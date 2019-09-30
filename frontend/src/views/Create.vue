<template>
  <div class="home">
    <div class="row">
      <div class="col">
      </div>
      <div class="col-6">
        <div class="card">
          <div class="card-body">
            <!-- <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a> -->
            <Form/>
          </div>
        </div>
      </div>
      <div class="col">
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Form from '@/components/Form.vue'

export default {
  name: 'create',
  components: {
    Form
  }
}
</script>