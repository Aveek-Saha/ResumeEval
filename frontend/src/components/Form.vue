<template>
  <form method="post">

    <div v-show="step === 0">
      <h4 class="card-title">Template Selector</h4>
      <div class="form-group">
        <div class="row">
    <div class="col-lg-6">
      <button @click.prevent="selectedTemplate(1)">
          <img src="../assets/1.png" width="100%" class="thumbnail img-responsive">
      </button>
            
    </div>
 <div class="col-lg-6">
      <button @click.prevent="selectedTemplate(2)">
          <img src="../assets/2.png" width="100%" class="thumbnail img-responsive">
      </button>
            
    </div>
  <div class="col-lg-6">
      <button @click.prevent="selectedTemplate(3)">
          <img src="../assets/3.png" width="100%" class="thumbnail img-responsive">
      </button>
            
    </div>
   <div class="col-lg-6">
      <button @click.prevent="selectedTemplate(4)">
          <img src="../assets/4.png" width="100%" class="thumbnail img-responsive">
      </button>
            
    </div>
  </div>

      </div>
    </div>

    <div v-show="step === 1">
      <h4 class="card-title">Personal Info</h4>
      <div class="form-group">
        <label>Full Name</label>
        <input type="text" class="form-control" v-model="name" placeholder="Enter your name" />
      </div>
      <div class="form-group">
        <label>Email address</label>
        <input type="email" class="form-control" v-model="email" placeholder="Enter email" />
        <small
          id="emailHelp"
          class="form-text text-muted"
        >We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label>Phone number</label>
        <input type="tel" class="form-control" v-model="number" placeholder="Enter Number" />
      </div>
      <div class="form-group">
        <label>Location</label>
        <input type="text" class="form-control" v-model="location" placeholder="Location" />
      </div>
      <div class="form-group">
        <label>Link</label>
        <input type="text" class="form-control" v-model="link" placeholder="Website link" />
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
        <button class="btn btn-primary" @click.prevent="sendData()">Preview</button>
      </div>

      <!-- <legend for="name">Your Name:</legend>
    <input id="name" name="name" v-model="registration.name">

    <legend for="email">Your Email:</legend>
      <input id="email" name="email" type="email" v-model="registration.email">-->
    </div>

    <div v-show="step === 2">
      <h4 class="card-title">Education</h4>
      <div v-for="(school, index) in education" v-bind:key="index">
        <div class="form-group">
          <label>School Name</label>
          <input
            type="text"
            class="form-control"
            v-model="school.institution"
            placeholder="School/University name"
          />
        </div>
        <div class="form-group">
          <label>Location</label>
          <input
            type="text"
            class="form-control"
            v-model="school.location"
            placeholder="School location"
          />
        </div>
        <div class="form-group">
          <label>Degree</label>
          <input
            type="tel"
            class="form-control"
            v-model="school.studyType"
            placeholder="Degree awarded"
          />
        </div>
        <div class="form-group">
          <label>Major</label>
          <input type="text" class="form-control" v-model="school.area" placeholder="Major" />
        </div>
        <div class="form-group">
          <label>GPA</label>
          <input
            type="number"
            class="form-control"
            v-model="school.gpa"
            placeholder="Grade point average"
          />
        </div>
        <div class="form-group">
          <label>Start date</label>
          <input type="date" class="form-control" v-model="school.startDate" placeholder="Date started" />
        </div>
        <div class="form-group">
          <label>End date</label>
          <input type="date" class="form-control" v-model="school.endDate" placeholder="Date ended" />
        </div>
        <div class="btn-group" role="group" style="text-align: right">
          <button class="btn btn-outline-success" @click.prevent="addEducation()">Add</button>
          <button class="btn btn-outline-danger" @click.prevent="delEducation(index)">Del</button>
        </div>
        <hr />
      </div>
      <br />

      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
        <button class="btn btn-primary" @click.prevent="sendData()">Preview</button>
      </div>
    </div>

    <div v-show="step === 3">
      <h4 class="card-title">Work</h4>
      <div v-for="(job, index) in work" v-bind:key="index">
        <div class="form-group">
          <label>Company Name</label>
          <input type="text" class="form-control" v-model="job.company" placeholder="Company name" />
        </div>
        <div class="form-group">
          <label>Location</label>
          <input
            type="text"
            class="form-control"
            v-model="job.location"
            placeholder="Office location"
          />
        </div>
        <div class="form-group">
          <label>Title</label>
          <input type="text" class="form-control" v-model="job.position" placeholder="Job title" />
        </div>
        <div class="form-group">
          <label>Responsibilities</label>
          <textarea
            class="form-control"
            v-model="job.highlights"
            placeholder="Enter each responsibility on a new line"
            rows="3"
          ></textarea>
        </div>
        <div class="form-group">
          <label>Start date</label>
          <input type="date" class="form-control" v-model="job.startDate" placeholder="Date started" />
        </div>
        <div class="form-group">
          <label>End date</label>
          <input type="date" class="form-control" v-model="job.endDate" placeholder="Date ended" />
        </div>
        <div class="btn-group" role="group" style="text-align: right">
          <button class="btn btn-outline-success" @click.prevent="addWork()">Add</button>
          <button class="btn btn-outline-danger" @click.prevent="delWork(index)">Del</button>
        </div>
        <hr />
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
        <button class="btn btn-primary" @click.prevent="sendData()">Preview</button>
      </div>
    </div>

    <div v-show="step === 4">
      <h4 class="card-title">Skills</h4>
      <div v-for="(skill, index) in skills" v-bind:key="index">
        <div class="form-group">
          <label>Name</label>
          <input type="text" class="form-control" v-model="skill.name" placeholder="Skill name" />
        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">Description</label>
          <textarea
            class="form-control"
            rows="3"
            v-model="skill.keywords"
            placeholder="Enter each point on a new line"
          ></textarea>
        </div>
        <div class="btn-group" role="group" style="text-align: right">
          <button class="btn btn-outline-success" @click.prevent="addSkill()">Add</button>
          <button class="btn btn-outline-danger" @click.prevent="delSkill(index)">Del</button>
        </div>
        <hr />
      </div>

      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
        <button class="btn btn-primary" @click.prevent="sendData()">Preview</button>
      </div>
    </div>

    <div v-show="step === 5">
      <h4 class="card-title">Projects</h4>
      <div v-for="(project, index) in projects" v-bind:key="index">
        <div class="form-group">
          <label>Title</label>
          <input
            type="text"
            class="form-control"
            v-model="project.name"
            placeholder="Project title"
          />
        </div>
        <div class="form-group">
          <label>Description</label>
          <input
            type="text"
            class="form-control"
            v-model="project.description"
            placeholder="Enter email"
          />
        </div>
        <div class="form-group">
          <label>Link</label>
          <input
            type="text"
            class="form-control"
            v-model="project.url"
            placeholder="Link to the project"
          />
        </div>
        <div class="form-group">
          <label>Tools used</label>
          <input
            type="text"
            class="form-control"
            v-model="project.keywords"
            placeholder="Seperate each tool with a comma"
          />
        </div>
        <div class="btn-group" role="group" style="text-align: right">
          <button class="btn btn-outline-success" @click.prevent="addProject()">Add</button>
          <button class="btn btn-outline-danger" @click.prevent="delProject(index)">Del</button>
        </div>
        <hr />
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="next()">Next</button>
        <button class="btn btn-primary" @click.prevent="sendData()">Preview</button>
      </div>
    </div>

    <div v-show="step === 6">
      <h4 class="card-title">Awards</h4>
      <div v-for="(award, index) in awards" v-bind:key="index">
        <div class="form-group">
          <label>Name</label>
          <input
            type="text"
            class="form-control"
            v-model="award.title"
            placeholder="Name of the award"
          />
        </div>
        <div class="form-group">
          <label>Date</label>
          <input
            type="text"
            class="form-control"
            v-model="award.date"
            placeholder="Date of recieving"
          />
        </div>
        <div class="form-group">
          <label>Summary</label>
          <textarea
            class="form-control"
            v-model="award.summary"
            rows="3"
            placeholder="About the award"
          ></textarea>
        </div>
        <div class="btn-group" role="group" style="text-align: right">
          <button class="btn btn-outline-success" @click.prevent="addAward()">Add</button>
          <button class="btn btn-outline-danger" @click.prevent="delAward(index)">Del</button>
        </div>
        <hr />
      </div>
      <div class="btn-group" role="group">
        <button class="btn btn-primary" @click.prevent="prev()">Back</button>
        <button class="btn btn-primary" @click.prevent="sendData(); next()">Submit</button>
        <button class="btn btn-primary" @click.prevent="sendData()">Preview</button>
      </div>
    </div>
    <div v-show="step === 7">
      <h5>Your Rating !!</h5>
     {{rating}}
    </div>
  </form>
</template>


<style>
.form-group {
  text-align: left;
}
</style>

<script>
import { async } from "q";
import axios from "axios"

export default {
  name: "Form",
  components: {},
  data() {
    return {
      template : 1,
      step: 0,
      rateUrl: "http://localhost:5001/rate",
      url: "http://localhost:9000/api/generate/resume",
      rating: "",
      name: null,
      email: null,
      number: null,
      location: null,
      link: null,
      education: [
        {
          institution: null,
          location: null,
          studyType: null,
          area: null,
          gpa: null,
          startDate: null,
          endDate: null
        }
      ],
      work: [
        {
          company: null,
          position: null,
          location: null,
          startDate: null,
          endDate: null,
          highlights: null
        }
      ],
      skills: [
        {
          name: null,
          keywords: null
        }
      ],
      projects: [
        {
          name: null,
          description: null,
          url: null,
          keywords: null
        }
      ],
      awards: [
        {
          title: null,
          date: null,
          summary: null
        }
      ]
    };
  },
  methods: {
    prev() {
      this.step--;
    },
    next() {
      this.step++;
    },
    selectedTemplate(idx) {
      this.template = idx;
      this.next();
    },
    addEducation() {
      this.education.push({
        institution: null,
        location: null,
        studyType: null,
        area: null,
        gpa: null,
        startDate: null,
        endDate: null
      });
    },
    delEducation(index) {
      if (this.education.length == 1) return;
      this.education.splice(index, 1);
    },
    addWork() {
      this.work.push({
        company: null,
        position: null,
        location: null,
        startDate: null,
        endDate: null,
        highlights: null
      });
    },
    delWork(index) {
      if (this.work.length == 1) return;
      this.work.splice(index, 1);
    },
    addSkill() {
      this.skills.push({
        name: null,
        keywords: null
      });
    },
    delSkill(index) {
      if (this.skills.length == 1) return;
      this.skills.splice(index, 1);
    },
    addProject() {
      this.projects.push({
        name: null,
        description: null,
        url: null,
        keywords: null
      });
    },
    delProject(index) {
      if (this.projects.length == 1) return;
      this.projects.splice(index, 1);
    },
    addAward() {
      this.awards.push({
        title: null,
        date: null,
        summary: null
      });
    },
    delAward(index) {
      if (this.awards.length == 1) return;
      this.awards.splice(index, 1);
    },
    sendData() {
      var self = this;
      var selectedTemplate = this.template;
      var sections = [
        "profile",
        "education",
        "work",
        "skills",
        "projects",
        "awards"
      ];
      var name = this.name;
      var email = this.email;
      var phone = this.number;
      var location = this.location;
      var website = this.link;
      var basics = {
        name,
        email,
        phone,
        location,
        website
      };
      var education = this.education;
      var work = this.work;
      var skills = [];
      this.skills.forEach(element => {
        if (element.name!= null) {
          skills.push({
            name: element.name,
            keywords: element.keywords.split(',')
          }) 
        }
      });
      var projects = [];
      this.projects.forEach(proj => {
        if (proj.name!= null) {
          projects.push({
            name: proj.name,
            description: proj.description,
            url: proj,url,
            keywords: proj.keywords.split(',')
          })
        }
      })
      var awards = this.awards;

      var data = {
        selectedTemplate,
        sections,
        basics,
        education,
        work,
        skills,
        projects,
        awards
      };
      console.log(data);
      var that = this
      axios.post(this.rateUrl, data)
      .then(function (response) {
        console.log(response);
        that.rating = response.data.rating
      })
      .catch(function (error) {
        console.log(error);
      });

      (async () => {
        const { fetch } = window;
        const req = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
          credentials: "same-origin"
        };

        const res = await fetch(self.url, req);
        const blob = await res.blob();

        if (!res.ok) {
          console.log("[ERROR] Response Received")
        } else {
          console.log("[SUCCESS] Response Received", blob)
          var file = new Blob([blob], {type: 'application/pdf'});
          var fileURL = URL.createObjectURL(file);
          window.open(fileURL);
          // const url = URL.createObjectURL(blob)
          self.$emit('pdfGenerated', fileURL)
        }
      })()

    }
  }
};
</script>
