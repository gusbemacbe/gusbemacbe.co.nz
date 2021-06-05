const ctx = document.getElementById('myChart').getContext('2d');
const chart = new Chart(ctx, 
{
  type: 'bar',
  plugins: [ChartDataSource],
  options: 
  {
    daatasource: 
    {

      url: '/static/data/prefeitura-de-aparecida/aparecida-small-without-duplicates.csv'
    }
  }
});