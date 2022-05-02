const ctx = document.getElementById("stat-chart").getContext("2d")

fetch("http://127.0.0.1:5000/top-insurer")
    .then(resp => resp.json())
    .then(data => {
        let labels = []
        let takenInsurances = []
        let revenues = []
        for (d of data) {
            labels.push(d.NAME + ` (${d.TAKEN_INSURANCE} db)`)        
            takenInsurances.push(parseInt(d.TAKEN_INSURANCE))  
            revenues.push(d.REVENUE)
        }

        const myChart = new Chart(ctx, {
            data: {
                labels: labels,
                datasets: [{
                    type: 'bar',
                    label: "Biztosítócégek kötött biztosításai és bevételei",
                    data: revenues,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.3)',
                        'rgba(123, 99, 222, 0.3)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132)',
                        'rgba(123, 99, 222)',

                    ],
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })
    })

    fetch("http://127.0.0.1:5000/stat")
    .then(resp => resp.json())
    .then(data => {
        console.log(data)
        $('#avg-age').text(data[0].AVG_AGE)
        $('#sum-trips-price').text(data[0].SUM_TRIPS_PRICE)
        $('#travellers-num').text(data[0].TRAVELLERS_NUM)

    })
