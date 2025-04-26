<script setup>
import NavView from './Views/NavView.vue';
</script>

<template>
  <div class="common-layout">
    <el-container>
        <el-aside>
            <NavView />
        </el-aside>
        <el-container>
            <el-header>
              <div class="header-content">
                <h3 >Home</h3>
                <h3 >Welcome To HomeAI</h3>
              </div>
            </el-header>
            <el-main>
              <router-view class="main-content"/>
              <!--
              <div class="main-content">
              </div>
-->
            </el-main>
<!--
            <el-footer>
            </el-footer>
-->
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.el-aside {
/*  background-color: blue; */
  position: fixed;
  left: 0px;
  width: 200px;
  height: 100%;
  top: 0px;
}
.el-header {
/*  background-color: indianred; */
  position: fixed;
  top: 0px;
  left:200px;
  height: 10%;
  width: calc(100% - 200px);
  border: 10px;
}
.el-main {
/*  background-color: lightblue; */
  position: fixed;
  top: 10%;
  left: 200px;
  width: calc(100% - 200px);
  height: 90%;

  display: flex;
  justify-content: center;
  justify-items: center;
}
.header-content  {
  display: flex;
/*  justify-content: space-between; */
  justify-content: space-around;
}
.main-content {
/*  display: flex; 
  justify-content: center;
  justify-items: center; 
  align-items: center;
*/
  width: 100%;
}



</style>
