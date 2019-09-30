<template>
<form action="https://postman-echo.com/post" method="post">
  <div v-show="step === 1">

    <h1>Step One</h1>
    
    <legend for="name">Your Name:</legend>
    <input id="name" name="name" v-model="registration.name">

    <legend for="email">Your Email:</legend>
    <input id="email" name="email" type="email" v-model="registration.email">

    <br>
    <button @click.prevent="next()">Next</button>
    
  </div>

  <div v-show="step === 2">
    <h1>Step Two</h1>
    
    <legend for="street">Your Street:</legend>
    <input id="street" name="street" v-model="registration.street">


    <legend for="city">Your City:</legend>
    <input id="city" name="city" v-model="registration.city">


    <legend for="state">Your State:</legend>
    <input id="state" name="state" v-model="registration.state">

    <br>
    <button @click.prevent="prev()">Previous</button>
    <button @click.prevent="next()">Next</button>

  </div>

  <div v-show="step === 3">
    <h1>Step Three</h1>
    
    <legend for="numtickets">Number of Tickets:</legend>
    <input id="numtickets" name="numtickets" type="number" v-model="registration.numtickets">

    <legend for="shirtsize">Shirt Size:</legend>
    <select id="shirtsize" name="shirtsize" v-model="registration.shirtsize">
      <option value="S">Small</option>
      <option value="M">Medium</option>
      <option value="L">Large</option>
      <option value="XL">X-Large</option>
    </select>
    <br>

    <button @click.prevent="prev()">Previous</button>
    <input type="submit" value="Save">
    
  </div>
  </form>
</template>


<style>

</style>

<script>
export default {
  name: 'Form',
  components: {
  },
  data() {
    return {
      step:1,
      registration:{
        name:null,
        email:null,
        street:null,
        city:null,
        state:null,
        numtickets:0,
        shirtsize:'XL'
      }
    }
  },
  methods: {
    prev() {
        this.step--;
    },
    next() {
        this.step++;
    }
  }
}
</script>
