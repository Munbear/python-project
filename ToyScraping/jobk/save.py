import csv 

def save_to_file(jobkorea_jobs):
  file = open("jobkorea.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","link"])
  for job in jobkorea_jobs:
    writer.writerow(list(job.values()))
  return