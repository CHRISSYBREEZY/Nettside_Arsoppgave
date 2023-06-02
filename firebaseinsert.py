from firebase import firebase


firebase = firebase.FirebaseApplication("https://login-for-kubemon-default-rtdb.firebaseio.com/", None)
data = {
    'Name':'Christopher Matre',
    'Email':'christophermatrealim@gmail.com',
    'Phone':45483104

}

result = firebase.post('https://login-for-kubemon-default-rtdb.firebaseio.com/:' data)
print(result)