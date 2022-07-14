$(document).ready(function () {

    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        method: 'POST',
        url: '/super_admin/',
        data: {
            csrfmiddlewaretoken: token


        },

        success: function (chart_data) {
            console.log('dataaa', chart_data)
            var order_status = chart_data.order_status
            var monthly_sale = chart_data.monthly_sale
            const orderData = {
                labels: [
                    'Pending',
                    'Success',
                    'Shipped',
                    'Deliverd',
                    'Cancelled',
                    'Return'
                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: order_status,
                    backgroundColor: [
                        'rgb(9, 88, 145',
                        'rgb(18, 14, 135)',
                        'rgb(205, 224, 61',
                        'rgb(9, 145, 16)',
                        'rgb(145, 7, 10)',
                        'rgb(209, 60, 23)'
                    ],
                    hoverOffset: 1
                }]
            };

            const orderConfig = {
                type: 'doughnut',
                data: orderData,
            };

            const orderChart = new Chart(
                document.getElementById('order-status-chart'),
                orderConfig
            );

            console.log('order_status', order_status)




            const labels = [
                'Sixth Last 30dys',
                'Fifth Last 30dys',
                'Fourth Last 30dys',
                'Third Last 30dys',
                'Second Last 30dys',
                'Last 30dys',
            ];

            const data = {
                labels: labels,
                datasets: [{
                    label: 'My First dataset',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(9, 156, 31)',
                    data: monthly_sale,
                }]
            };

            const config = {
                type: 'line',
                data: data,
                options: {}
            };
            const myChart = new Chart(
                document.getElementById('sales-chart'),
                config
            );

        }

    })


})
