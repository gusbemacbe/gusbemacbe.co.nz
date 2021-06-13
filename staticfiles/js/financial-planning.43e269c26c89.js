// Tables caption
const food = document.querySelector('table.food');
food.id = "food";

const bills = document.querySelector('table.bills');
bills.id = "bills";

const medicaments = document.querySelector('table.medicaments');
medicaments.id = "medicaments";

const shopping = document.querySelector('table.shopping');
shopping.id = "shopping";

const supermarket = document.querySelector('table.supermarket');
supermarket.id = "supermarket";

document.getElementById("bills").createCaption().textContent = "Contas mensais";
document.getElementById("food").createCaption().textContent = "Comida";
document.getElementById("medicaments").createCaption().textContent = "Remédios";
document.getElementById("shopping").createCaption().textContent = "Compras";
document.getElementById("supermarket").createCaption().textContent = "Supermercado";

// Current minimum wage rates in New Zealand
const locale = 'pt-BR';
const options = { year: 'numeric', month: 'long', day: 'numeric' };

const week = (hour) =>
{
  const week = hour * 40;
  return week
}

const month = (hour) =>
{
  const month = (hour * 40) * 4;
  return month
}

const year = (hour) =>
{
  const year = ((hour * 40) * 4) * 12;
  return year
}

const kFormatter = (num) =>
{
  return Math.abs(num) > 999 ? Math.sign(num) * ((Math.abs(num) / 1000).toFixed(1)) + 'k' : Math.sign(num)*Math.abs(num)
}

const minimum_wage = new Vue({ 
  el: '#minimum-wage',
  delimiters: ['[[', ']]'],
  data: 
  {
    adult: 20,
    trainee: 16,
    date: new Date(Date.UTC(2021, 03, 01, 15, 12, 0)).toLocaleDateString(locale, options),
  },
  computed: 
  {
    adult_week: 
    function () 
    {
      return week(this.adult)
    },
    trainee_week: 
    function () 
    {
      return week(this.trainee)
    },
    adult_month: 
    function () 
    {
      return month(this.adult)
    },
    trainee_month: 
    function () 
    {
      return month(this.trainee)
    },
    adult_year: 
    function () 
    {
      return kFormatter(year(this.adult))
    },
    trainee_year: 
    function () 
    {
      return kFormatter(year(this.trainee))
    },
  }
});

// Average salary of a developer in New Zealand
const minimum = 50000
const average = 65000
const maximium = 95000

const salary_of_a_developer = new Vue({ 
  el: '#salary-of-a-developer',
  delimiters: ['[[', ']]'],
  data: 
  {
      average_monthly_salary: Math.round(average / 12),
      maximium_monthly_salary: Math.round(maximium / 12),
      minimum_monthly_salary: Math.round(minimum / 12),
      average_weekly_salary: Math.round((average / 12) / 4),
      maximium_weekly_salary: Math.round((maximium / 12) / 4),
      minimum_weekly_salary: Math.round((minimum / 12) / 4)
  }
});