from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("customer_orders_Spark")
sc = SparkContext(conf = conf)

def split_rows(row):
    all_rows = row.split(',')
    return (int(all_rows[0]), float(all_rows[2]))

path = '/tmp/spark/Book'
input = sc.textFile(path)
rdd = input.map(split_rows)
customer_orders = rdd.reduceByKey(lambda x, y: x + y)

results = customer_orders.collect();
for result in results:
    print(result)