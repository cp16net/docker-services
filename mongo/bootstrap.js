db = connect("localhost:27017/auth");
db.users.insert({ email: "test@test.com", key: "user", secret: "pass" } );
