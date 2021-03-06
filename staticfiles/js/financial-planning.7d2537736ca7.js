// Tables caption

const office = document.querySelectorAll('.office');

for (let i = 0; i < office.length; i++) 
{
  const caption = office[i].createCaption();
  caption.textContent = "Escritório";
}

const pre_travel = document.querySelectorAll('.pre-travel');

for (let i = 0; i < pre_travel.length; i++) 
{
  const caption = pre_travel[i].createCaption();
  caption.textContent = "Pré-viagem";
}

const comparison = document.querySelectorAll('.comparison-1');

for (let i = 0; i < comparison.length; i++) 
{
  const caption = comparison[i].createCaption();
  caption.textContent = "Salário mensal mínimo de um adulto ou estagiário";
}

const uy_comparison = document.querySelectorAll('.uy-comparison-1');

for (let i = 0; i < uy_comparison.length; i++) 
{
  const caption = uy_comparison[i].createCaption();
  caption.textContent = "Salário mínimo mensal";
}

const developer = document.querySelectorAll('.comparison-2');

for (let i = 0; i < developer.length; i++) 
{
  const caption = developer[i].createCaption();
  caption.textContent = "Salário mensal de um desenvolvedor";
}

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

// Current minimum wage in Uruguay
const uy_minimum_wage = new Vue({ 
  el: '#minimum-wage-uruguay',
  delimiters: ['[[', ']]'],
  data: 
  {
    uy_date: new Date(Date.UTC(2021, 00, 01, 01, 01, 0)).toLocaleDateString(locale, options),
    uy_minimum: 17930
  },
  computed: 
  {
    uy_year:
    function () 
    {
      return kFormatter(this.uy_minimum * 12)
    },
  }
});

// Comaprisons
/** Minimum wage **/

const comparisons = new Vue({ 
  el: '#comparison-of-minimum-wages',
  delimiters: ['[[', ']]'],
  data: 
  {
    adult: 20,
    trainee: 16,
    uy_minimum_month: 17930
  },
  computed: 
  {
    nz_adult_minimum_month: 
    function () 
    {
      return month(this.adult)
    },
    nz_trainee_minimum_month: 
    function () 
    {
      return month(this.trainee)
    },
    uy_minimum_month_to_brl: 
    function () 
    {
      return this.uy_minimum_month * 0.12
    },
  }
});