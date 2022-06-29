var primaryColorShade = '#836AF9',
    yellowColor = '#ffe800',
    successColorShade = '#28dac6',
    warningColorShade = '#ffe802',
    warningLightColor = '#FDAC34',
    infoColorShade = '#299AFF',
    greyColor = '#4F5D70',
    blueColor = '#2c9aff',
    blueLightColor = '#84D0FF',
    greyLightColor = '#EDF1F4',
    tooltipShadow = 'rgba(0, 0, 0, 0.25)',
    lineChartPrimary = '#666ee8',
    lineChartDanger = '#ff4961',
    labelColor = '#6e6b7b',
    grid_line_color = 'rgba(200, 200, 200, 0.2)'; // RGBA color helps in dark layout

new Vue({
    el: '#envs',
    delimiters: ['[[', ']]'],
    data() {
        return {
            envs: [],
            tempData: [0, 10, 5, 2, 20, 30, 45],
        }
    },
    mounted() {

    },
    created() {
        this.getEnvironments();
    },
    methods: {
        getEnvironments() {
            /** Get all environments */
            new EnvironmentDataService().getState().then((response) => {
                return response.data;
            }).then(data => {
                this.envs = data; // set data to use in the vue element
                return data
            }).then( (resp) => {
                this.createTempUmdChart();
                this.createPowerConsumptionDonoutChart();
            }).then(resp => {
                this.makeAnalysis();
            }).then(resp => {
                console.log(this.envs[0])
            });

        },
        makeAnalysis() {
            for (var i = 0; i < this.envs.length; i++) {
                this.envs[i]['recommendations'] = {}
                this.envs[i]['recommendations_color'] = {}
            }

            for (var i = 0; i < this.envs.length; i++) {

                // first make the verification of the temperature
                if (this.envs[i].t_t >= this.envs[i]['curr_temp'].t_a) {
                    this.envs[i]['recommendations']['temp'] = 'Temperatura do ambiente está dentro do padrão desejado.';
                    this.envs[i]['recommendations_color']['temp'] = 'text-success';
                } else {
                    this.envs[i]['recommendations']['temp'] = 'Temperatura do ambiente está acima do padrão desejado.'
                    this.envs[i]['recommendations_color']['temp'] = 'text-danger';
                }

                // second: make the verification of the humidity
                if ( 50 <= this.envs[i]['curr_temp'].umd < 80) {
                    this.envs[i]['recommendations']['umd'] = 'Umidade do ambiente está dentro do padrão desejado.'
                    this.envs[i]['recommendations_color']['umd'] = 'text-success';
                } else {
                    this.envs[i]['recommendations']['umd'] = 'Umidade do ambiente está fora do padrão desejado.'
                    this.envs[i]['recommendations_color']['umd'] = 'text-danger';
                }

                // make the verification of the nocive gas
                if ( this.envs[i]['curr_temp'].n_g > 500) {
                    this.envs[i]['recommendations']['nocive_gas'] = 'Qualidade do ar está dentro dos padrões desejados.'
                    this.envs[i]['recommendations_color']['nocive_gas'] = 'text-success';
                } else {
                    this.envs[i]['recommendations']['nocive_gas'] = 'Qualidade do ar está fora do padrão desejado.'
                    this.envs[i]['recommendations_color']['nocive_gas'] = 'text-danger';
                }
            }

        },
        createTempUmdChart() {
            /** Create all charts for temp and umd of each environment */

            for (var i = 0; i < this.envs.length; i++) {

                let chartOptions = this.tempUmdLineChartOptions(this.envs[i]['sensor_data'])
                let elemId = this.envs[i].id;                                                   // get chart labels and data
                let elem = $(`canvas#${elemId}.temp-umd`);

                new Chart(
                    elem[0].getContext('2d'),                                                    //get canvas by id
                    chartOptions);                                                               // pass the chart options
            }
        },
        tempUmdLineChartOptions(data) {
            return {
                type: 'line',

                // The data for our dataset
                // it is required to reverse the arrays due to django erro in queryset.all()[-n:]
                data: {
                    labels: data.map(a => {
                        let currDate = new Date(a['created_at']);
                        return `${currDate.getHours()}:${currDate.getMinutes()}:${currDate.getSeconds()}`;
                    }).reverse(), // grab all datetime
                    datasets: [
                        {
                            label: 'Temperatura',
                            yAxisID: 'temp',
                            backgroundColor: 'rgba(255, 99, 132, 0.3)',
                            borderColor: 'rgb(255, 99, 132)',
                            data: data.map(val => val['t_a']).reverse() // get all current temperatures
                        },
                        {
                            label: 'Umidade',
                            yAxisID: 'umd',
                            backgroundColor: 'rgba(115, 103, 240, 0.3)',
                            borderColor: 'rgb(115, 103, 240)',
                            data: data.map(val => val['umd']).reverse() // get all current temperatures
                        }
                    ]
                },

                // Configuration options go here
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    backgroundColor: false,
                    hover: {
                        mode: 'label'
                    },
                    tooltips: {
                        // Updated default tooltip UI
                        shadowOffsetX: 1,
                        shadowOffsetY: 1,
                        shadowBlur: 8,
                        shadowColor: tooltipShadow,
                        backgroundColor: window.colors.solid.white,
                        titleFontColor: window.colors.solid.black,
                        bodyFontColor: window.colors.solid.black
                    },
                    scales: {
                        xAxes: [
                            {
                                display: true,
                                scaleLabel: {
                                    display: true
                                },
                                gridLines: {
                                    display: true,
                                    color: grid_line_color,
                                    zeroLineColor: grid_line_color
                                },
                                ticks: {
                                    fontColor: labelColor
                                }
                            }
                        ],
                        yAxes: [
                            {
                                id: 'temp',
                                position: 'left',
                                display: true,
                                scaleLabel: {
                                    display: true
                                },
                                ticks: {
                                    stepSize: 5,
                                    min: 0,
                                    max: 50,
                                    color: grid_line_color,
                                    zeroLineColor: grid_line_color
                                }
                            },
                            {
                                id: 'umd',
                                position: 'right',
                                display: true,
                                scaleLabel: {
                                    display: true
                                },
                                ticks: {
                                    stepSize: 10,
                                    min: 0,
                                    max: 100,
                                    color: grid_line_color,
                                    zeroLineColor: grid_line_color
                                }
                            },
                        ],
                    },
                    legend: {
                        display: false
                    }
                },

            }
        },
        createPowerConsumptionDonoutChart() {
            for (var i = 0; i < this.envs.length; i++) {

                //let chartOptions = this.tempUmdLineChartOptions(this.envs[i]['sensor_data'])                          // get chart labels and data
                let chartOptions = this.powerConsumptionChartOptions()

                let elemId = this.envs[i].id;                                                   // get chart labels and data
                let elem = $(`canvas#${elemId}.power-consumption-dougnut-chart`);

                new Chart(
                    elem[0].getContext('2d'),                                                   //get canvas by id
                    chartOptions);                                                              // pass the chart options
            }
        },
        powerConsumptionChartOptions() {
            return {
                type: 'doughnut',
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    responsiveAnimationDuration: 500,
                    cutoutPercentage: 60,
                    legend: {display: false},
                    tooltips: {
                        callbacks: {
                            label: function (tooltipItem, data) {
                                var label = data.datasets[0].labels[tooltipItem.index] || '',
                                    value = data.datasets[0].data[tooltipItem.index];
                                var output = ' ' + label + ' : ' + value + ' %';
                                return output;
                            }
                        },
                        // Updated default tooltip UI
                        shadowOffsetX: 1,
                        shadowOffsetY: 1,
                        shadowBlur: 8,
                        shadowColor: tooltipShadow,
                        backgroundColor: window.colors.solid.white,
                        titleFontColor: window.colors.solid.black,
                        bodyFontColor: window.colors.solid.black
                    }
                },
                data: {
                    datasets: [
                        {
                            labels: ['Refrigeração', 'Iluminação'],
                            data: [85, 15],
                            backgroundColor: [window.colors.solid.primary, warningLightColor],
                            borderWidth: 0,
                            pointStyle: 'rectRounded'
                        }
                    ]
                }
            }
        }

    }
});
