<template>
<form action="https://postman-echo.com/post" method="post">
  <div v-show="step === 1">
    <h4 class="card-title">Personal Info</h4>
      <div class="form-group">
        <label >Full Name</label>
        <input type="text" class="form-control" v-model="name"  placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label>Email address</label>
        <input type="email" class="form-control" v-model="email" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label >Phone number</label>
        <input type="tel" class="form-control" v-model="number" placeholder="Enter Number">
      </div>
      <div class="form-group">
        <label >Location</label>
        <input type="text" class="form-control" v-model="location" placeholder="Location">
      </div>
      <div class="form-group">
        <label >Link</label>
        <input type="text" class="form-control" v-model="link" placeholder="Website link">
      </div>
      <button class="btn btn-primary" @click.prevent="next()">Next</button>

    <!-- <legend for="name">Your Name:</legend>
    <input id="name" name="name" v-model="registration.name">

    <legend for="email">Your Email:</legend>
    <input id="email" name="email" type="email" v-model="registration.email"> -->
    
  </div>

  <div v-show="step === 2">
    <h4 class="card-title">Education</h4>
        <div v-for="(school, index) in education" v-bind:key="index">
          <div class="form-group">
            <label >School Name</label>
            <input type="text" class="form-control" v-model="school.name" placeholder="School/University name">
          </div>
          <div class="form-group">
            <label >Location</label>
            <input type="text" class="form-control" v-model="school.location" placeholder="School location">
          </div>
          <div class="form-group">
            <label>Degree</label>
            <input type="tel" class="form-control" v-model="school.degree" placeholder="Degree awarded">
          </div>
          <div class="form-group">
            <label >Major</label>
            <input type="text" class="form-control" v-model="school.major" placeholder="Major">
          </div>
          <div class="form-group">
            <label >GPA</label>
            <input type="number" class="form-control" v-model="school.gpa" placeholder="Grade point average">
          </div>
          <div class="form-group">
            <label >Start date</label>
            <input type="text" class="form-control" v-model="school.start" placeholder="Date started">
          </div>
          <div class="form-group">
            <label >End date</label>
            <input type="text" class="form-control" v-model="school.end" placeholder="Date ended">
          </div>
          <div class="btn-group" role="group" style="text-align: right">
            <button class="btn btn-outline-success" @click.prevent="addEducation()">Add</button>
            <button class="btn btn-outline-danger" @click.prevent="delEducation(index)">Del</button>
          </div>
        <hr>
        </div>
        <br>

      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 3">
    <h4 class="card-title">Work</h4>
      <div v-for="(job, index) in work" v-bind:key="index">
        <div class="form-group">
          <label >Company Name</label>
          <input type="text" class="form-control" v-model="job.name" placeholder="Company name">
        </div>
        <div class="form-group">
          <label>Location</label>
          <input type="text" class="form-control" v-model="job.location" placeholder="Office location">
        </div>
        <div class="form-group">
          <label >Title</label>
          <input type="text" class="form-control" v-model="job.title" placeholder="Job title">
        </div>
        <div class="form-group">
          <label >Responsibilities</label>
          <textarea class="form-control" v-model="job.responsibilities" placeholder="Enter each responsibility on a new line" rows="3"></textarea>
        </div>
        <div class="form-group">
          <label >Start date</label>
          <input type="text" class="form-control" v-model="job.start" placeholder="Date started">
        </div>
        <div class="form-group">
          <label >End date</label>
          <input type="text" class="form-control" v-model="job.end" placeholder="Date ended">
        </div>
        <div class="btn-group" role="group" style="text-align: right">
            <button class="btn btn-outline-success" @click.prevent="addWork()">Add</button>
            <button class="btn btn-outline-danger" @click.prevent="delWork(index)">Del</button>
          </div>
        <hr>
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 4">
    <h4 class="card-title">Skills</h4>
      <div v-for="(skill, index) in skills" v-bind:key="index">
        <div class="form-group">
          <label >Name</label>
          <input type="text" class="form-control" v-model="skill.name" placeholder="Skill name">
        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">Description</label>
          <textarea class="form-control" rows="3" v-model="skill.description" placeholder="Enter each point on a new line"></textarea>
        </div>
        <div class="btn-group" role="group" style="text-align: right">
            <button class="btn btn-outline-success" @click.prevent="addSkill()">Add</button>
            <button class="btn btn-outline-danger" @click.prevent="delSkill(index)">Del</button>
          </div>
        <hr>
      </div>
      
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 5">
    <h4 class="card-title">Projects</h4>
    <div v-for="(project, index) in projects" v-bind:key="index">
      <div class="form-group">
        <label >Title</label>
        <input type="text" class="form-control" v-model="project.name" placeholder="Project title">
      </div>
      <div class="form-group">
        <label>Description</label>
        <input type="text" class="form-control" v-model="project.description" placeholder="Enter email">
      </div>
      <div class="form-group">
        <label >Link</label>
        <input type="text" class="form-control" v-model="project.link" placeholder="Link to the project">
      </div>
      <div class="form-group">
        <label >Tools used</label>
        <input type="text" class="form-control" v-model="project.tools" placeholder="Seperate each tool with a comma">
      </div>
      <div class="btn-group" role="group" style="text-align: right">
          <button class="btn btn-outline-success" @click.prevent="addProject()">Add</button>
          <button class="btn btn-outline-danger" @click.prevent="delProject(index)">Del</button>
        </div>
      <hr>
    </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
      </div>
  </div>

  <div v-show="step === 6">
    <h4 class="card-title">Awards</h4>
      <div class="form-group">
        <label >Award Name</label>
        <input type="text" class="form-control"   placeholder="Enter your name">
      </div>
      <div class="form-group">
        <label >Date</label>
        <input type="text" class="form-control"   placeholder="Location">
      </div>
      <div class="form-group">
        <label >Summary</label>
        <input type="text" class="form-control"   placeholder="Location">
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
      name:null,
      email:null,
      number: null,
      location: null,
      link: null,
      education: [{
        name: null,
        location: null,
        degree: null,
        major: null,
        gpa: null,
        start: null,
        end: null
      }],
      work: [{
          name: null,
          title: null,
          location: null,
          start: null,
          end: null,
          responsibilities: null
      }],
      skills: [{
        name: null,
        description: null
      }],
      projects: [{
          name: null,
          description: null,
          link: null,
          tools: null
      }],
      awards: [{
          name: null,
          date: null,
          summary: null
      }]
    }
  },
  methods: {
    prev() {
        this.step--;
    },
    next() {
        this.step++;
    },
    addEducation(){
      this.education.push({
        name: null,
        location: null,
        degree: null,
        major: null,
        gpa: null,
        start: null,
        end: null
      })
    },
    delEducation(index){
      if(this.education.length == 1)
        return;
      this.education.splice(index, 1)
      
    },
    addWork(){
      this.work.push({
        name: null,
        title: null,
        location: null,
        start: null,
        end: null,
        responsibilities: null
      })
    },
    delWork(index){
      if(this.work.length == 1)
        return;
      this.work.splice(index, 1)
      
    },
    addSkill(){
      this.skills.push({
        name: null,
        description: null
      })
    },
    delSkill(index){
      if(this.skills.length == 1)
        return;
      this.skills.splice(index, 1)
      
    },
    addProject(){
      this.projects.push({
          name: null,
          description: null,
          link: null,
          tools: null
      })
    },
    delProject(index){
      if(this.projects.length == 1)
        return;
      this.projects.splice(index, 1)
      
    },
  }
}
</script>
