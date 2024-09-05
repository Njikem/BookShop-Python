from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement
from helpers import check_endpoint_info 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# user's functions

@app.post('/api/user')
def insert_user():
    valid_check = check_endpoint_info(request.json, ['first_name', 'last_name', 'address', 'phone_number', 'email', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_user(?, ?, ?, ?, ?, ?)", [request.json.get("first_name"), request.json.get("last_name"),request.json.get("address"),  request.json.get("phone_number"), request.json.get("email"),  request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)



@app.get('/api/users')
def get_users(): 

    try: 
        results = run_statement("CALL get_user()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    


@app.patch("/api/users")
def update_users():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_user_token(?)", [token])
    print(results[0]['id'])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['email', 'password'])

    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_user(?, ?, ?)", [results[0]['id'], request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify('user info updated successfully'), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    


@app.delete('/api/users')
def delete_users():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_user_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_user(?, ?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    



# User's Login functions

@app.post('/api/user_login')
def post_users_login():
    valid_check = check_endpoint_info(request.json, ['email', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL login_user(?, ?)", [ request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)

    
@app.delete('/api/users_login')
def delete_users_login():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_user_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_login(?, ?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    


#functions for bookshop

# function to Post bookshop

@app.post('/api/bookshop')
def insert_bookshop():
    valid_check = check_endpoint_info(request.json, ['name', 'email', 'password', 'address', 'phone_number'])  
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_bookshop(?, ?, ?, ?, ?)", [request.json.get("name"), request.json.get("email"),  request.json.get("password"), request.json.get("address"),  request.json.get("phone_number")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    



# function to get the bookshop

@app.get('/api/bookshops')
def get_bookshop(): 
    try: 
        results = run_statement("CALL get_bookshop()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)



#function to update the bookshop

@app.patch("/api/bookshop")
def update_bookshop():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_bookshop_token(?)", [token])
    print(results[0]['id'])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['email', 'password'])

    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_bookshop(?, ?, ?)", [results[0]['id'], request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify('Bookshop info is updated successfully'), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)


# Function to delete bookshop

@app.delete('/api/bookshop')
def delete_bookshop():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_bookshop_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_bookshop(?, ?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)





# Bookshop login functions

# post login function

@app.post('/api/bookshop_login')
def post_bookshop_login():
    valid_check = check_endpoint_info(request.json, ['email', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL bookshop_login(?, ?)", [ request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)



#function to delete bookshop login

@app.delete('/api/bookshop')
def delete_bookshop_login():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_user_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_bookshop_login(?, ?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200) 
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    




# Books functions


# post books function
@app.post('/api/books')
def post_books():
    token = request.headers.get("Authorization")
    print(token, type(token))
    results = run_statement("CALL verified_bookshop_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    bookshop_id = results[0]['id']
    print(bookshop_id)
    
    
    valid_check = check_endpoint_info(request.json, [ 'image_url', 'name', 'title', 'description', 'price', 'author', 'category', 'stock'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)

    results = run_statement("CALL post_books(?, ?, ?, ?, ?, ?, ?, ?, ?)", [bookshop_id, request.json.get("image_url"), request.json.get("name"), request.json.get("title"), request.json.get("description"), request.json.get("price"),request.json.get("author"), request.json.get("category"), request.json.get("stock")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    



# function to get the books

@app.get('/api/books')
def get_books(): 
    try: 
        results = run_statement("CALL get_books()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400) 


#Get books by id

@app.get('/api/books/<int:book_id>')
def get_book_by_id(book_id): 
    try: 
        results = run_statement("CALL get_books()", [book_id])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results[0]), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400) 




# Update books
@app.patch("/api/books")
def update_books():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_bookshop_token(?)", [token])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['id','image_url', 'name', 'price'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_book(?, ?, ?, ?)", [ request.json.get("id"), request.json.get("image_url"), request.json.get("name"), request.json.get("price")])
    print(results)
    print(request.json)
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    

    # delete books
    #come back

@app.delete('/api/books')
def delete_books():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_bookshop_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['id'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_books(?)", ['id'])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200) 
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)





# user's order functions


# Post user_order

@app.post('/api/user_order')
def post_userOrder():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_user_token(?)", [token])
    user_id = results[0]['id']
    print(user_id)
   
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, [ 'books', 'bookshop_id'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    books = request.json.get('books')
   
    bookshop_id = request.json.get('bookshop_id')
    
   #Step
    for book in books:
        print(book)
        results = run_statement("CALL check_books(?, ?)", [book, bookshop_id])
        print(results)
        if(len(results) ==0):
            return make_response(jsonify('Sorry, something went wrong.'), 400)
   
    #Step2
    results = run_statement("CALL post_orders(?, ?)", [user_id,  bookshop_id])
    print(results)
    order_id = results[0]['id']
    print(order_id) 
   
    #step3
    for book in books:
      results = run_statement("CALL post_order_books(?, ?)", [order_id, book])
      

    return make_response(jsonify({'order_id':order_id}), 200)



# Get user_order

@app.get('/api/user_order')
def get_user_order(): 

    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_user_token(?)", [token])
    print('Check out', results[0]['id'])
    if(len(results) == 0): 
            return 'token invalid'
    user_id = results[0]['id']
    print(user_id)
  
    results = run_statement("CALL get_user_order(?)", [user_id])
    if(len(results) == 0): 
            return 'You do not have any orders in the system'
    return make_response(jsonify(results), 200)
    




#Bookshop order functions   


# Patch bookshop order

@app.patch("/api/bookshop_order")
def update_bookshop_order():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_bookshop_token(?)", [token])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['order_id', 'is_confirmed', 'is_complete'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_order(?, ?, ?)", [ request.json.get("order_id"), request.json.get("is_confirmed"), request.json.get("is_complete")])
    print(results)
    print(request.json)
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    



    #function for search Bar
    
@app.get('/api/search')
def search_bar(): 
 search_term = request.args.get('q')
 if not search_term:
    return make_response(jsonify({"error": "A search term is required."}), 400)

 try:
        # Pass the search term to the stored procedure
        results = run_statement("CALL search_books(%s)", [search_term])
        print(f"Results from database: {results}") 
        if results is None:
            return make_response(jsonify({"error": "Something went wrong with the search."}), 500)
        return make_response(jsonify(results), 200)
 except Exception as err:
        print(err)
        return make_response(jsonify({"error": str(err)}), 400)



app.run(debug=True)
