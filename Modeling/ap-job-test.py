import dask.multiprocessing

# wrap our code with the following line since we use the "python obama_job.py > obama_job.out" format in our sbatch obamaJob file 
if __name__ == '__main__':
  dask.config.set(scheduler='processes', num_workers = 16) # multiprocessing is the default
    # (num_workers must match the cpus-per-task that we set in the obamaJob file)
  

  import numpy as np
  from sklearn.linear_model import LinearRegression
  from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
  import dask.dataframe as dd
  
  ap = dd.read_csv('/accounts/campus/rhiann_zhang/ap_model.csv')
  apX = ap[['teachers_per_student', 'students_chronically_absent', 'enrl_gifted_talented']]
    
  import time
  t0 = time.time() # time.time() gets time in seconds since epoch 

  
  # Run exhaustive search with linear regression
  y = np.array(ap['AP_oneormore_relative'])
  X = np.array(apX)
  lr = LinearRegression()

  efs = EFS(lr, 
            min_features=1,
            max_features=3,
            scoring='neg_mean_squared_error',
            cv=5,
            print_progress = True,
            n_jobs = 4)

  efs.fit(X, y)

  print('Best MSE score: %.2f' % efs.best_score_ * (-1))
  print('Best subset:', efs.best_idx_)
  
  
  # Return the time that has passed since the t0 = time.time() line was executed
  # i.e. times how long it took to read in the data and do the filtering 
  print(time.time() - t0)
  # This allows us to get a sense for how much time is involved working with this much data 

