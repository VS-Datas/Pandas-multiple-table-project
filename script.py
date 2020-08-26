import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#print(visits)   
#print(cart)                    
#print(checkout)
#print(purchase)

visits_cart_leftm = pd.merge(visits, cart, how= 'left')
#print(visits_cart_leftm)

len_visits_cart_leftm = len(visits_cart_leftm)
#print(len_visits_cart_leftm)

null_cart_time = len(visits_cart_leftm[visits_cart_leftm.cart_time.isnull()])

#print(null_cart_time)

#print(float(null_cart_time) / len_visits_cart_leftm) 

cart_checkout_left = pd.merge(cart, checkout, how= 'left')
#print(cart_checkout_left)

len_cart_checkout = len(cart_checkout_left)

null_count = len(cart_checkout_left[cart_checkout_left.isnull()])
#print(null_count)
#print(float(len_cart_checkout) / (null_count))

checkout_pruchase = pd.merge(checkout, purchase, how='left')
#print(checkout_pruchase)
len_checkout_pruchase = len(checkout_pruchase)

purchase_null = len(checkout_pruchase[checkout_pruchase.purchase_time.isnull()])
#print(purchase_null)

#print(float(len_checkout_pruchase) /(purchase_null))


all_data = visits.merge(cart, how='left')\
   .merge(checkout, how='left')\
   .merge(purchase, how='left')

#print(all_data.head())
len_all_data = len(all_data)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
#print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())





























