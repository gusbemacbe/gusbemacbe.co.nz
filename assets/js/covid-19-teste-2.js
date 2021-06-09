const agesCSV = async () => 
{
  const array = []
  await d3.csv("/static/data/gustavo/confirmados/aparecida-casos-e-mortes-por-faixa-etária.csv", data => { array.push(data)});
  return array;
}

const makeChart = async () => 
{

  const ages = await agesCSV()
  const ageLabels = ages.map(a => a.age);

  const ageFemaleCases = ages.filter((person) => 
  {
    return person.sex === 'FEMININO';
  })

  const ageMaleCases = ages.filter((person) => 
  {
    return person.sex === 'MASCULINO';
  })

  const isDeathFemaleCases = ages.reduce((person) => 
  {
    return person.isDeath == "1";
  })

  const isDeathMaleCases = ages.reduce((person) => 
  {
    return person.isDeath == "1";
  })

  const conditions = (predicates) => (item) => {
    return predicates.map((predicate) => predicate(item)).every(Boolean);
  };

  const isMale = ({ sex }) => sex === "MASCULINO";
  const isFemale = ({ sex }) => sex === "FEMININO";
  const isAdult = ({ age }) => +age > 19 && +age < 60;
  const isDead = ({ ISDeath }) => !!Number(ISDeath);

  const isDeadAdultMale = conditions([isDead, isMale, isAdult]);
  const isDeadAdultFemale = conditions([isDead, isFemale, isAdult]);

  const deadAdultMales = ages.filter(isDeadAdultMale);
  const deadAdultFemales = ages.filter(isDeadAdultFemale);

  const cases_by_age = new Chart('CasesbyAge',
  {
    type: "bar",
    data: 
    {
      labels: ["0-10", "11-15", "16-24", "25-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"],
      datasets: 
      [
        {
          color: "rgba(226, 117, 169, 1)",
          backgroundColor: "rgba(226, 117, 169, 1)",
          borderColor: "rgba(226, 117, 169, 1)",
          data: deadAdultFemales,
          label: "Female"
        },
        {
          color: "rgba(113, 205, 248, 1)",
          backgroundColor: "rgba(113, 205, 248, 1)",
          borderColor: "rgba(113, 205, 248, 1)",
          data: deadAdultMales,
          label: "Male"
        }
      ]
    },
    options: 
    {
      indexAxis: 'y',
      elements: {
        bar: {
          borderWidth: 2,
        }
      },
      responsive: true,
      scales: 
      {
        yAxes: 
        [{
            stacked: true
        }],
        xAxes: 
        [{
            stacked: false
        }]
      }
    },
  })

}

makeChart();