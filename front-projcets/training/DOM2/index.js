const signup = () => {
  let elem_username = document.getElementById("username");
  let elem_password = document.getElementById("password");
  let elem_age = document.getElementById("age");
  let username = elem_username.value;
  let password = elem_password.value;
  let age = elem_age.value;

  validate(elem_username);
  validate(elem_password);
  validate(elem_age);

  console.log(elem_username);
};

let a = 'maktab'