fetch("http://127.0.0.1:5000/timetable")
    .then(resp => resp.json())
    .then(data => {
        console.log(data)
        let iter = 1
        for (d of data) {
            $("#timetable-body").append(`
                <tr>
                    <th scope="row">${iter++}</th>
                    <td>${d.FROM_CITY}</td>
                    <td>${d.TO_CITY}</td>
                    <td>${d.TAKEOFF_TIME}</td>
                    <td>${d.LANDING_TIME}</td>
                    <td>${d.AIRLINE_NAME}</td>
                    <td>${d.PRICE} Ft</td>
                </tr>
            `)
        }
    })


fetch("http://127.0.0.1:5000/popular")
    .then(resp => resp.json())
    .then(data => {
        let iter = 1
        console.log(data)
        for (d of data) {
            $("#popular-body").append(`
                <tr>
                    <th scope="row">${iter++}</th>
                    <td>${d.NAME}</td>
                    <td>${d.NUM}</td>
                </tr>
            `)
        }
    })


const ctx = document.getElementById("stat-chart").getContext("2d")

fetch("http://127.0.0.1:5000/popular")
    .then(resp => resp.json())
    .then(data => {
        let labels = []
        let numOfTicket = []
        let label =  "Legnépszerűbb város"
        for (d of data) {
            labels.push(d.NAME)
            numOfTicket.push(d.NUM)
        }
        console.log(labels)
        console.log(numOfTicket)

        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: numOfTicket,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.3)',
                        'rgba(54, 162, 235, 0.3)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132)',
                        'rgba(54, 162, 235)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'x',
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })
    })


