function validate(element) {
    if (element.value == "") {
     return element.style.cssText = "border: red 1px solid";
    } else {
      element.style.cssText = "border: none";
    }
    if (element.id == "username") {
      element.value.length < 6 ?
        (document
          .getElementById("username-helper").style.cssText ="display: inline") : (document
              .getElementById("username-helper").style.cssText ="display: none")
    }
    else if (element.id == "password") {
      element.value.length <= 3 ?
       ( document
          .getElementById("password-helper")
          .style.cssText = "display: inline") : (document
              .getElementById("password-helper").style.cssText ="display: none")
    }
   else if (element.id == "age") {
      typeof +element.value !='number' ?
        (document
          .getElementById("age-helper")
          .style.cssText = "display: inline") : (document
              .getElementById("age-helper").style.cssText ="display: none")
    }
  }

  alert(a)