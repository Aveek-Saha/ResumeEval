<template>
  <div class="home">
    <div class="row">
      <div class="col-lg-6 col-md-12 col-sm-12">
        <div class="card">
          <div class="card-body">
            <Form @pdfGenerated="handlePdfGenerated" />
          </div>
        </div>
      </div>

      <div class="col-lg-6 d-none d-lg-block">
        <div class="card">
          <div class="card-body">
            <Preview v-bind:pdfUrl="pdfUrl" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Form from "@/components/Form.vue";
import Preview from "@/components/Preview.vue";

export default {
  name: "create",
  components: {
    Form,
    Preview
  },
  data() {
    return {
      pdfUrl: null
    };
  },
  methods: {
    handlePdfGenerated(response) {
      this.pdfUrl = response;
      console.log("[INFO] Received Event ", this.pdfUrl);
    }
  }
};
</script>