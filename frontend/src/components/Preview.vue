<template>
  <div>
    <div class="row">
      <!-- <input v-model.number="page" type="number" style="width: 5em" />
      /{{numPages}}
      <button @click="rotate += 90">&#x27F3;</button>
      <button @click="rotate -= 90">&#x27F2;</button>
      <button @click="$refs.pdf.print()">print</button> -->
  <div class="col-sm-12"> 
        <a v-bind:href="pdfUrl" target="_blank"> <button class="btn btn-outline-success">Download</button></a>
    
    </div>
    </div>

    <div class="row">
      <div 
        v-if="loadedRatio > 0 && loadedRatio < 1"
        style="background-color: green; color: white; text-align: center"
        :style="{ width: loadedRatio * 100 + '%' }"
      >{{ Math.floor(loadedRatio * 100) }}%</div>
      <div class="col-12">
        <pdf
          v-if="show"
          ref="pdf"
          style="width:100%;border: 2px solid black"
          v-bind:src="pdfUrl"
          :page="page"
          :rotate="rotate"
          @progress="loadedRatio = $event"
          @error="error"
          @num-pages="numPages = $event"
          @link-clicked="page = $event"
        ></pdf>
      </div>
    </div>
  </div>
</template>
<script>
import pdf from "vue-pdf";

export default {
  components: {
    pdf: pdf
  },
  data() {
    console.log("HELLO");
    
    return {
      show: true,
      loadedRatio: 0,
      page: 1,
      numPages: 0,
      rotate: 0
    };
  },
  props : [
    'pdfUrl'
  ],
  methods: {
    error: function(err) {
      console.log("[ERROR] in error() of Preview.vue", err);
    }
  },
   watch: {
        pdfUrl : function(val, oldVal){
        console.log("[OLD] ", oldVal)
        console.log("[NEW] ", val)
      }
    }
};
</script>