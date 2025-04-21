<script setup>
    import { reactive, ref, onMounted, defineProps } from 'vue'
    import * as echarts from 'echarts';
    const props = defineProps({
        funcDataLoader: {
            type: Function,
            required: false 
        }
    });
    var data = ref(0)
    var lineChart_Data = reactive({
        x: [1, 2, 3, 4, 5],
        y: [7, 4, 3, 1, 5]
    })

    onMounted(() => {
        console.log("LineChart")
        console.log(props.funcDataLoader())
        data.value = props.funcDataLoader()

        var dom = document.getElementById('main')
        var myChart = echarts.init(dom);

        var option = {
            xAxis: {
                type: 'value',
                data : lineChart_Data.x
            },
            yAxis: {},
            series:[
                {
                    data: lineChart_Data.y,
                    type: 'line'
                }
            ]
        }

        myChart.setOption(option)
    })
</script>
<template>
    <div id="main" style="width: 800px;height:600px;"></div>
</template>

<style scoped>
</style>