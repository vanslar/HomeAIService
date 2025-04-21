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

    })
</script>
<template>
    <div id="main" style="width: 100%;height:100%;"></div>
</template>
<style scoped></style>