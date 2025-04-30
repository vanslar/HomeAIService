<script setup>
import { ref, reactive, nextTick } from 'vue'
import { RequestInfo } from '../../Utils/WebIO.js'

const LLMURL = 'http://127.0.0.1:5001/LLMService/ResponsePrompt'

class ChatMessage{
    constructor(content, role){
        this.content = content
        this.role = role
    }
}
const ViewData = reactive({
    messages: [
    ]
})

const chatMessagesRef = ref(null)
const disableInputButtonRef = ref(false)

const inputMessage = ref('')
const sendMessage = async () => {
    if (inputMessage.value.trim() !== '') {
        ViewData.messages.push(new ChatMessage(inputMessage.value, 'client'))
        //使能input按钮
        disableInputButtonRef.value = true
        var post_response = await askLLM(LLMURL, 'POST', inputMessage.value)
        ViewData.messages.push(new ChatMessage(post_response, 'model'))

        inputMessage.value = ''
        disableInputButtonRef.value = false 
        // 等待 DOM 更新完成后滚动到最新消息
        nextTick(() => {
            if (chatMessagesRef.value) {
                chatMessagesRef.value.scrollTop = chatMessagesRef.value.scrollHeight
            }
        })
    }
}

const askLLM = async (url, method, prompt) => {
    var data = {
        'prompt': prompt
    }
    var response = await RequestInfo(url, method, data)
    return response 

}
</script>

<template>
    <div class="chat-container">
        <div class="chat-messages" ref="chatMessagesRef">
            <li v-for="(message, index) in ViewData.messages" :key="index" :class="message.role === 'model' ? 'model-response' : 'client-request'">
                {{ message.content }}
            </li>
        </div>

        <div class="input-container">
            <el-input
                v-model="inputMessage"
                placeholder="请输入消息"
                :rows="3"
                type="textarea"
                resize="none"
            />
            <el-button type="primary" class="send-button" :disabled="disableInputButtonRef" @click="sendMessage">发送</el-button>
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
/*
.message {
    width: 70%;
    border-radius: 10px;
}
*/
.model-response {
    align-self: flex-start;
    background-color: #f4f4f5;

    color: #000000; /* 设置文字颜色为黑色 */
}

.client-request {
    align-self: flex-end;
    background-color: #e6f7ff;
    color: #000000; /* 设置文字颜色为黑色 */
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