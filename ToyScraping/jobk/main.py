from kjob import jk_jobs_information as job_korea
from save import save_to_file

jobkorea_jobs = job_korea()

save_to_file(jobkorea_jobs)
