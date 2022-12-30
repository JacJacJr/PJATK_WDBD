from mrjob.job import MRJob
from mrjob.step import MRStep			

class CustomerOrders(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_id_orders,
                  reducer=self.reducer_sum_orders),
            MRStep(mapper=self.mapper_orders_id,
                   reducer=self.reducer_sorted)
        ]	
        	
    def mapper_id_orders(self, _, line):
        # lines items: customer_id, item_id, order_amount (with ',' separator). Item_id is unnecesery 
        (customer_id, _, order_amount) = line.split(',')
        #return groups of orders, in order: key-ID, value-order
        yield customer_id, float(order_amount)		

    #sum all amounts for keys - ID
    def reducer_sum_orders(self, customer_id, order_amount):
        yield customer_id, sum(order_amount) 		

    #Reverse groups - keys are the amount
    def mapper_orders_id(self, customer_id, order_amount):
        #None for better processing
        yield None, (order_amount, customer_id)			
    
    #sort by keys
    def reducer_sorted(self, _, order_amounts):	
        for order_amount, customer_id in sorted(order_amounts):
            #%f is decimal format for float values
             yield customer_id, '%04.02f'%float(order_amount) #format 


if __name__ == '__main__':
    CustomerOrders.run()
