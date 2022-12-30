from mrjob.job import MRJob

class CustomerOrders(MRJob):

    def mapper(self, _, line):
        # lines items: customer_id, item_id, order_amount (with ',' separator). Item_id is unnecesery 
        (customer_id, _, order_amount) = line.split(',')
        #return groups of orders, in order: key-ID, value-order
        yield customer_id, float(order_amount)		

    #sum and round all amounts for keys - ID
    def reducer(self, customer_id, order_amount):
        yield customer_id, round(sum(order_amount), 2)

if __name__ == '__main__':
    CustomerOrders.run()
