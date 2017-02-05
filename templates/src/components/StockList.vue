<template>
  <div id="stockList">
  <el-table
      :data="stockList"
      stripe
      border>
      <el-table-column
        prop="code"
        label="代码">
        <template scope="scope">
          <el-button
          size="small"
          @click="changeCode(scope.row.code)">{{ scope.row.code }}</el-button>
        </template>
</el-table-column>
<el-table-column prop="name" label="名称">
</el-table-column>
<el-table-column prop="c_name" label="行业">
</el-table-column>
</el-table>
</div>
</template>

<script>
    export default {
        name: 'stockList',
        data() {
            return {
                stockList: null
            }
        },
        created: function() {
            this.$http.get('/stock/list').then(response => {
                this.stockList = response.body
            }, response => {
                // error callback
            });
        },
        methods: {
            changeCode(code) {
                console.log('点击：' + code)
                this.$store.commit('changeCode', {
                    code: code
                });
            }
        }
    }
</script>