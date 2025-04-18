<script setup>
    import LineChart from '../../components/ChartView/LineChart.vue'
    const funcDataLoader = () => {
        return {
            x: [1, 2, 3, 4, 5],
            y: [7, 4, 3, 1, 5]
        }
    }
</script>

<template>
    <div>
        <h1>Test</h1>
        <LineChart :funcDataLoader="funcDataLoader" />
    </div>
</template>

<style scoped>
</style>