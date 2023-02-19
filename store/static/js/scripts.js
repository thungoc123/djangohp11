/*!
 * Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
 * Copyright 2013-2022 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project
var btns = document.getElementsByClassName("addtocart");

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    location.reload()

    if (user === "AnonymousUser") {
      console.log("User is not logged in");
    } else {
      updateCart(productId, action);
    }
  });
}
function updateCart(id, action) {
  let url = "/updatecart";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: id, action: action })
      
  })
  .then((response) => response.json())
  .then((data) => console.log(data))
  
}

let quantityField = document.getElementsByClassName('quantity')
for (let i = 0; i < quantityField.length; i++) {
    quantityField[i].addEventListener('change', function() {
        let quantityFieldValue = quantityField[i].value
        let quantityFieldProduct = quantityField[i].parentElement.parentElement.children[1].children[0].innerText
        alert(quantityFieldProduct)
        location.reload()
        let url = "/updatequantity"
        fetch(url, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({ "qfv": quantityFieldValue, "qfp": quantityFieldProduct, })
            })
            .then(response => response.json())
            .then(data => console.log(data))
    })
}