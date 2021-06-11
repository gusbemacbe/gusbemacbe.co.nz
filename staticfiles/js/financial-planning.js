const food = document.querySelector('table.food');
food.id = "food"

const bills = document.querySelector('table.bills');
bills.id = "bills"

const shopping = document.querySelector('table.shopping');
shopping.id = "shopping"

const supermarket = document.querySelector('table.supermarket');
supermarket.id = "supermarket"

document.getElementById("bills").createCaption().innerHTML = "<b>Contas mensais</b>"; 
document.getElementById("food").createCaption().innerHTML = "<b>Comida</b>"; 
document.getElementById("shopping").createCaption().innerHTML = "<b>Compras</b>"; 
document.getElementById("supermarket").createCaption().innerHTML = "<b>Supermercado</b>"; 