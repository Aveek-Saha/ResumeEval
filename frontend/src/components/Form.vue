<template>
<form action="https://postman-echo.com/post" method="post">
  <div v-show="step === 1">
    <h4 class="card-title">Personal Info</h4>
      <div class="form-group">
        <label for="exampleInputPassword1">Full Name</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Phone number</label>
        <input type="tel" class="form-control" id="exampleInputPassword1" placeholder="Enter Number">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Location</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Link</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter a URL">
      </div>
      <button class="btn btn-primary" @click.prevent="next()">Next</button>

    <!-- <legend for="name">Your Name:</legend>
    <input id="name" name="name" v-model="registration.name">

    <legend for="email">Your Email:</legend>
    <input id="email" name="email" type="email" v-model="registration.email"> -->
    
  </div>

  <div v-show="step === 2">
    <h4 class="card-title">Education</h4>
      <div class="form-group">
        <label for="exampleInputPassword1">School Name</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label for="exampleInputEmail1">School Location</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Degree</label>
        <input type="tel" class="form-control" id="exampleInputPassword1" placeholder="Enter Number">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Major</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">GPA</label>
        <input type="number" class="form-control" id="exampleInputPassword1" placeholder="Enter a URL">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Start date</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">End date</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 3">
    <h4 class="card-title">Work</h4>
      <div class="form-group">
        <label for="exampleInputPassword1">Company Name</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label for="exampleInputEmail1">Location</label>
        <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Title</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter Number">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Responsibilities</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Start date</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">End date</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 4">
    <h4 class="card-title">Skills</h4>
      <div class="form-group">
        <label for="exampleInputPassword1">Skill Name</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label for="exampleInputEmail1">Details</label>
        <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
      </div>
      
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 5">
    <h4 class="card-title">Projects</h4>
      <div class="form-group">
        <label for="exampleInputPassword1">Project Name</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label for="exampleInputEmail1">Description</label>
        <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Link</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter Number">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Tools used</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 6">
    <h4 class="card-title">Awards</h4>
      <div class="form-group">
        <label for="exampleInputPassword1">Award Name</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Date</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Summary</label>
        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Location">
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
  </div>
  </form>
</template>


<style>
.form-group{
  text-align: left;
}
</style>

<script>
export default {
  name: 'Form',
  components: {
  },
  data() {
    return {
      step:1,
      school: {
        name: null,
        location: null,
        degree: null,
        major: null,
        gpa: null,
        start: null,
        end: null
      },
      job: {
          company_name: null,
          title: null,
          location: null,
          start: null,
          end: null,
          responsibilities: []
      },
      project: {
          name: null,
          description: null,
          link: null,
          tools: []
      },
      award: {
          name: null,
          date: null,
          summary: null
      },
      registration:{
        name:null,
        email:null,
        location: null,
        link: null,
        education: [],
        work: [],
        skills: [],
        projects: [],
        awards: []
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
