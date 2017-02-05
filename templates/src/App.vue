<template>
  <div id="app">
<el-row :gutter="20">
  <el-col :span="6">
    <stockList></stockList>
  </el-col>
  <el-col :span="18">
    <stockKline></stockKline>
  </el-col>
    </el-row>
  </div>
</template>

<script>
    import stockList from './components/StockList'
    import stockKline from './components/StockKline'

    export default {
        name: 'app',
        components: {
            stockList,
            stockKline
        }
    }
</script>