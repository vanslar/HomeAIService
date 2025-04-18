<script setup>
    import { ref, onMounted, defineProps } from 'vue'
    const props = defineProps({
        funcDataLoader: {
            type: Function,
            required: false 
        }
    });
    var data = ref(0)

    onMounted(() => {
        console.log("LineChart")
        console.log(props.funcDataLoader())
        data.value = props.funcDataLoader()

    })
</script>
<template>
    <h1>LineChart</h1>
    <h3>{{ data.x }}</h3>
    <h3>{{ data.y }}</h3>
</template>
<style scoped></style>