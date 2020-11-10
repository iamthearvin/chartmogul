from chartmogul import *
config = Config('e88a0c644867aaf8c93aac1ba7dbf927', '5104aef3baa833a189084a300c56d9f0')
  
try:
  Ping.ping(config).get()
  print("Connection successful.")
except err as e:
  print("Connection failed.")

mrr = Metrics.mrr(
    config,
    start_date="2019-01-01",
    end_date="2019-04-30",
    interval="month").get()

print("Total MRR for Q1 2019:\n")
for e in mrr.entries:
  print(e.date.strftime('%B')+": "+str(e.mrr/100))

mrr = Metrics.mrr(
    config,
    start_date="2019-04-01",
    end_date="2019-07-31",
    interval="month").get()

print("\n\nTotal MRR for Q2 2019:\n")
for e in mrr.entries:
  print(e.date.strftime('%B')+": "+str(e.mrr/100))
