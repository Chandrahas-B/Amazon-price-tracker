function plot_graph(scraped_times, prices)
{
        prices.unshift(0);
        scraped_times.unshift(0);
        const data = {
            labels: scraped_times,
            datasets: [{
                label: 'Price history',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: prices,
            }]
        };
 
        const config = {
            type: 'line',
            data: data,
            options: { maintainAspectRatio: false }
        };
 
        const myChart = new Chart(
            document.getElementById('myChart'),
            config
        );
}
