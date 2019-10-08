<template>
  <div class="home">
    <div class="row">
      <div class="col">
      </div>
      <div class="col-6">
        <div class="card">
          <div class="card-body">
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