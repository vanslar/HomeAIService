<script setup>
import { ref } from 'vue'

const inputMessage = ref('')
</script>

<template>
    <div class="chat-container">
        <div class="chat-messages">
            <el-card class="message model-response">
                <div>
                    <p>Model Response</p>
                    <p>Model Response</p>
                </div>
            </el-card>

            <el-card class="message client-request">
                <div>
                    <p>Client Request</p>
                    <p>Client Request</p>
                </div>
            </el-card>
        </div>

        <div class="input-container">
            <el-input
                v-model="inputMessage"
                placeholder="请输入消息"
                :rows="3"
                type="textarea"
                resize="none"
            />
            <el-button type="primary" class="send-button">发送</el-button>
        </div>
    </div>
</template>

<style scoped>
.chat-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.message {
    width: 70%;
    border-radius: 10px;
}

.model-response {
    align-self: flex-start;
    background-color: #f4f4f5;
}

.client-request {
    align-self: flex-end;
    background-color: #e6f7ff;
}

.input-container {
    position: sticky;
    width: 100%;
    bottom: 0;
    padding: 20px;
    background-color: white;
    border-top: 1px solid #dcdfe6;
    display: flex;
    gap: 10px;
}

.send-button {
    align-self: flex-end;
}
</style>