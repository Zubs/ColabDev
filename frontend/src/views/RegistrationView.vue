<template>
  <div>
    <NavBar />
    <div class="background-container">
      <section class="content">
        <!-- Wrapping the heading and paragraph in a div with a background box -->
        <div class="text-box">
          <h1 class="move-rightheader">Undergraduate Open Day Booking Form</h1>
        </div>
        <p class="move-right">
          Please use this form to book an On-Campus Undergraduate Open Day. <br />We're looking
          forward to seeing you!
        </p>
      </section>
    </div>
    <section class="ftco-section">
      <div class="container">
        <div class="row block-9">
          <div class="col-md-12 d-flex">
            <form @submit.prevent="submitForm" class="px-5 contact-form w-100">
              <div class="section-heading mb-4">
                <h3 class="h4">Personal Details</h3>
              </div>
              <div class="form-row">
                <div class="form-group col-md-3">
                  <label for="title">Title*</label>
                  <select id="title" v-model="formData.title" class="form-control">
                    <option value="">Please select</option>
                    <option value="Mr">Mr</option>
                    <option value="Mrs">Mrs</option>
                    <option value="Miss">Miss</option>
                    <option value="Ms">Ms</option>
                    <option value="Dr">Dr</option>
                    <option value="Prof">Prof</option>
                    <option value="Mx">Mx</option>
                    <option value="Other">Other</option>
                  </select>
                  <span v-if="errors.title" class="text-danger">{{ errors.title }}</span>
                </div>
                <div class="form-group col-md-4">
                  <label for="firstName">First Name*</label>
                  <input
                    type="text"
                    id="firstName"
                    v-model="formData.firstName"
                    class="form-control"
                  />
                  <span v-if="errors.firstName" class="text-danger">{{ errors.firstName }}</span>
                </div>
                <div class="form-group col-md-5">
                  <label for="lastName">Last Name*</label>
                  <input
                    type="text"
                    id="lastName"
                    v-model="formData.lastName"
                    class="form-control"
                  />
                  <span v-if="errors.lastName" class="text-danger">{{ errors.lastName }}</span>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="dob">Date of Birth*</label>
                  <input type="date" id="dob" v-model="formData.dob" class="form-control" />
                  <span v-if="errors.dob" class="text-danger">{{ errors.dob }}</span>
                </div>
              </div>
              <div class="form-row">
                <div class="checkbox-item">
                  <input type="checkbox" id="carerCheck" v-model="carer" class="mr-2" />
                  <label for="carerCheck">Are you coming with a parent/carer?</label>
                </div>
              </div>
              <div v-if="carer" class="section-heading mb-4 mt-5">
                <h3 class="h4">Carer Details (Optional)</h3>
              </div>
              <div v-if="carer" class="form-row">
                <div class="form-group col-md-6">
                  <label for="firstName">First Name*</label>
                  <input
                    type="text"
                    id="carerFirstName"
                    v-model="formData.carerFirstName"
                    class="form-control"
                  />
                  <span v-if="errors.carerFirstName" class="text-danger">{{
                    errors.carerFirstName
                  }}</span>
                </div>
                <div class="form-group col-md-6">
                  <label for="lastName">Last Name*</label>
                  <input
                    type="text"
                    id="carerLastName"
                    v-model="formData.carerLastName"
                    class="form-control"
                  />
                  <span v-if="errors.carerLastName" class="text-danger">{{
                    errors.carerLastName
                  }}</span>
                </div>
              </div>
              <div v-if="carer" class="form-row">
                <div class="form-group col-md-6">
                  <label for="email">Email Address*</label>
                  <input
                    type="text"
                    id="carerEmail"
                    v-model="formData.carerEmail"
                    class="form-control"
                  />
                  <span v-if="errors.carerEmail" class="text-danger">{{ errors.carerEmail }}</span>
                </div>
              </div>
              <div class="section-heading mb-4 mt-5">
                <h3 class="h4">Contact Details</h3>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="email">Email Address*</label>
                  <input type="text" id="email" v-model="formData.email" class="form-control" />
                  <span v-if="errors.email" class="text-danger">{{ errors.email }}</span>
                </div>
                <div class="form-group col-md-6">
                  <label for="phone">Phone Number*</label>
                  <input type="tel" id="phone" v-model="formData.phone" class="form-control" />
                  <span v-if="errors.phone" class="text-danger">{{ errors.phone }}</span>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-12">
                  <label for="address1">Address Line 1*</label>
                  <input
                    type="text"
                    id="address1"
                    v-model="formData.address1"
                    class="form-control"
                  />
                  <span v-if="errors.address1" class="text-danger">{{ errors.address1 }}</span>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-12">
                  <label for="address2">Address Line 2</label>
                  <input
                    type="text"
                    id="address2"
                    v-model="formData.address2"
                    class="form-control"
                  />
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-4">
                  <label for="city">Town/City*</label>
                  <input type="text" id="city" v-model="formData.city" class="form-control" />
                  <span v-if="errors.city" class="text-danger">{{ errors.city }}</span>
                </div>

                <div class="form-group col-md-4">
                  <label for="postcode">Postcode*</label>
                  <input
                    type="text"
                    id="postcode"
                    v-model="formData.postcode"
                    class="form-control"
                  />
                  <span v-if="errors.postcode" class="text-danger">{{ errors.postcode }}</span>
                </div>

                <div class="form-group col-md-4">
                  <label for="country">Country*</label>
                  <select id="country" v-model="formData.country" class="form-control">
                    <option value="">Please select</option>
                    <option v-for="(country, index) in countries" :key="index" :value="country">
                      {{ country }}
                    </option>
                  </select>
                  <span v-if="errors.country" class="text-danger">{{ errors.country }}</span>
                </div>
              </div>
              <div class="section-heading mb-4 mt-5">
                <h3 class="h4">Course Interests</h3>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="studyLevel">Level of Study*</label>
                  <select id="studyLevel" v-model="formData.studyLevel" class="form-control">
                    <option value="">Please select</option>
                    <option value="Undergraduate">Undergraduate</option>
                    <option value="Postgraduate">Postgraduate</option>
                    <option value="Research">Research</option>
                    <option value="International Foundation Year">
                      International Foundation Year
                    </option>
                  </select>
                  <span v-if="errors.studyLevel" class="text-danger">{{ errors.studyLevel }}</span>
                </div>
                <div class="form-group col-md-6">
                  <label for="subjectArea">Subject Area*</label>
                  <select id="subjectArea" v-model="formData.subjectArea" class="form-control">
                    <option value="">Please select</option>
                    <option v-for="(subject, index) in subjectAreas" :value="subject" :key="index">
                      {{ subject }}
                    </option>
                  </select>
                  <span v-if="errors.subjectArea" class="text-danger">{{
                    errors.subjectArea
                  }}</span>
                </div>
              </div>
              <div class="section-heading mb-4 mt-5">
                <h3 class="h4">Event Details</h3>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="eventDate">Event Date*</label>
                  <select id="eventDate" v-model="formData.eventDate" class="form-control">
                    <option value="">Please select</option>
                    <option v-for="(event, index) in eventDates" :key="index" :value="event.date">
                      {{ event.label }}
                    </option>
                  </select>
                  <span v-if="errors.eventDate" class="text-danger">{{ errors.eventDate }}</span>
                </div>
                <div class="form-group col-md-6">
                  <label>How many guests will you be bringing?*</label>
                  <select id="guestCount" v-model="formData.guestCount" class="form-control">
                    <option value="">Please select</option>
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                  </select>
                  <span v-if="errors.guestCount" class="text-danger">{{ errors.guestCount }}</span>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-12">
                  <label>How did you hear about this event?*</label>
                  <div class="checkbox-grid">
                    <div class="checkbox-item">
                      <input
                        type="checkbox"
                        id="source_email"
                        v-model="formData.sources.email"
                        class="mr-2"
                      />
                      <label for="source_email">Email</label>
                    </div>
                    <div class="checkbox-item">
                      <input
                        type="checkbox"
                        id="source_social"
                        v-model="formData.sources.social"
                        class="mr-2"
                      />
                      <label for="source_social">Social Media</label>
                    </div>
                    <div class="checkbox-item">
                      <input
                        type="checkbox"
                        id="source_search"
                        v-model="formData.sources.search"
                        class="mr-2"
                      />
                      <label for="source_search">Search Engine</label>
                    </div>
                    <div class="checkbox-item">
                      <input
                        type="checkbox"
                        id="source_school"
                        v-model="formData.sources.school"
                        class="mr-2"
                      />
                      <label for="source_school">School/College</label>
                    </div>
                    <div class="checkbox-item">
                      <input
                        type="checkbox"
                        id="source_other"
                        v-model="formData.sources.other"
                        class="mr-2"
                      />
                      <label for="source_other">Other</label>
                    </div>
                  </div>
                  <span v-if="errors.sources" class="text-danger">{{ errors.sources }}</span>
                </div>
              </div>
              <div class="section-heading mb-4 mt-5">
                <h3 class="h4">Privacy Policy</h3>
              </div>
              <div class="form-row">
                <div class="checkbox-item">
                  <input type="checkbox" id="privacyPolicy" v-model="privacyPolicy" class="mr-2" />
                  <label for="privacyPolicy"
                    >I can confirm that I have read, understood, and agreed to the
                    <a
                      target="_blank"
                      href="https://www.wlv.ac.uk/about-us/governance/legal-information/corporate-compliance/data-protection/enquiry-and-website-request-privacy-notice/"
                      >Privacy Policy</a
                    ></label
                  >
                </div>
              </div>
              <span v-if="errors.privacyPolicy" class="text-danger">{{
                errors.privacyPolicy
              }}</span>
              <div class="form-group text-center mt-5">
                <button
                  type="submit"
                  class="btn btn-primary py-3 px-5 form-control"
                  :disabled="loading"
                >
                  <span v-if="loading">Processing...</span>
                  <span v-else>Register for Open Day</span>
                </button>
                <span v-if="errors.request" class="text-danger">{{ errors.request }}</span>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>

<style scoped>
/* Background container with an image */
.background-container {
  position: relative;
  background-image: url('https://study-net.eu/wp-content/uploads/2020/02/pic_3.jpg'); /* Path to your image */
  background-size: cover; /* Ensure the image covers the entire container */
  background-position: center; /* Center the image */
  min-height: 100vh; /* Full height */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 0; /* Layer the content above */
}

/* Apply the blur effect to the background image using a pseudo-element */
.background-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: inherit;
  background-size: cover;
  background-position: center;
  filter: blur(5px);
  z-index: -1;
}

/* Content area to display text */
.content {
  z-index: 1;
  position: relative;
  text-align: center;
}

@media (min-width: 1024px) {
  .events {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

/* Styling for the background box */
.text-box {
  background-color: lightyellow;
  padding: 5px; /* Add padding inside the box */
  border-radius: 5px; /* Rounded corners */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
  margin: 0 auto; /* Center the box horizontally */
}

.move-right {
  margin-left: 50px;
  font-size: 3ch;
  color: white;
}

.move-rightheader {
  margin-left: -21px; /* Ensure this font is available */
  font-size: 3rem; /* Add size to make the change more noticeable */
  font-weight: 900; /* Change font weight to make it bold */
  color: black;
}
</style>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { ref } from 'vue'
import api from '@/services/axios.js'

const formData = ref({
  title: '',
  firstName: '',
  lastName: '',
  dob: '',
  email: '',
  phone: '',
  address1: '',
  address2: '',
  city: '',
  postcode: '',
  country: '',
  studyLevel: '',
  subjectArea: '',
  eventDate: '',
  guestCount: '',
  sources: {
    email: false,
    social: false,
    search: false,
    school: false,
    other: false,
  },
  carerFirstName: '',
  carerLastName: '',
  carerEmail: '',
})
const errors = ref({
  title: '',
  firstName: '',
  lastName: '',
  dob: '',
  email: '',
  phone: '',
  address1: '',
  address2: '',
  city: '',
  postcode: '',
  country: '',
  studyLevel: '',
  subjectArea: '',
  eventDate: '',
  guestCount: '',
  sources: '',
  carerFirstName: '',
  carerLastName: '',
  carerEmail: '',
  privacyPolicy: '',
  request: '',
})
const countries = ref([
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo',
  'Costa Rica',
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Korea',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Korea',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
])
const subjectAreas = ref([
  'Accounting, Finance and Economics',
  'Animation and Games Design',
  'Architecture and Built Environment',
  'Art and Design',
  'Biological Sciences and Animal Behaviour',
  'Biomedical and Healthcare Sciences',
  'Business and Management',
  'Chemical Engineering',
  'Civil Engineering',
  'Community Health',
  'Computer Science and Cyber Security',
  'Continuing Professional Development - Education',
  'Continuing Professional Development - Health',
  'Criminology',
  'Early Childhood and Family Studies',
  'Education, Special Education Needs and Inclusion Studies',
  'Emergency and Disaster Management',
  'Engineering: Aerospace, Automotive and Mechanical',
  'English and Creative Writing',
  'Film, TV, Media and Journalism',
  'Forensic Science',
  'Health, Wellbeing and Social Care',
  'History, Politics and War Studies',
  'International Foundation Years',
  'International Pre-Masters / Pre-Sessionals',
  'Interpreting (BSL/English) and Deaf Studies',
  'Law',
  'Midwifery',
  'Nursing - Adult Nursing',
  "Nursing - Children's Nursing",
  'Nursing - Learning Disability Nursing',
  'Nursing - Mental Health Nursing',
  'Occupational Therapy',
  'Other Enquiry',
  'Paramedic Science',
  'Pharmacy, Pharmaceutical Science and Pharmacology',
  'Physiotherapy',
  'Podiatry',
  'Policing, Fire and Rescue',
  'Psychology',
  'Public Health',
  'Social Work',
  'Sociology and Social Policy',
  'Sport and Physical Activity',
  'Sustainability and Climate Change',
  'Teaching - Further Education',
  'Teaching - Primary',
  'Teaching - Secondary',
  'Tourism and Hospitality',
])
const eventDates = ref([
  { date: '2025-03-15', label: 'Saturday, 15 March 2025' },
  { date: '2025-04-19', label: 'Saturday, 19 April 2025' },
  { date: '2025-06-21', label: 'Saturday, 21 June 2025' },
  // TODO: Use API to fetch available event dates
])
const carer = ref(false)
const loading = ref(false)
const privacyPolicy = ref(false)

const validateForm = () => {
  errors.value = {
    title: '',
    firstName: '',
    lastName: '',
    dob: '',
    email: '',
    phone: '',
    address1: '',
    address2: '',
    city: '',
    postcode: '',
    country: '',
    studyLevel: '',
    subjectArea: '',
    eventDate: '',
    guestCount: '',
    sources: '',
    carerFirstName: '',
    carerLastName: '',
    carerEmail: '',
    privacyPolicy: '',
    request: '',
  }
  let isValid = true

  if (!formData.value.title) {
    errors.value.title = 'Please select a title'
    isValid = false
  }

  if (!formData.value.firstName) {
    errors.value.firstName = 'First name is required'
    isValid = false
  }

  if (!formData.value.lastName) {
    errors.value.lastName = 'Last name is required'
    isValid = false
  }

  if (!formData.value.dob) {
    errors.value.dob = 'Date of birth is required'
    isValid = false
  }

  if (carer.value) {
    if (!formData.value.carerFirstName) {
      errors.value.carerFirstName = 'Carer first name is required'
      isValid = false
    }

    if (!formData.value.carerLastName) {
      errors.value.carerLastName = 'Carer last name is required'
      isValid = false
    }

    if (!formData.value.carerEmail) {
      errors.value.carerEmail = 'Carer email is required'
      isValid = false
    }
  }

  if (!formData.value.email) {
    errors.value.email = 'Email is required'
    isValid = false
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.email)) {
    errors.value.email = 'Please enter a valid email address'
    isValid = false
  }

  if (!formData.value.phone) {
    errors.value.phone = 'Phone number is required'
    isValid = false
  }

  if (!formData.value.address1) {
    errors.value.address1 = 'Address line 1 is required'
    isValid = false
  }

  if (!formData.value.city) {
    errors.value.city = 'Town/City is required'
    isValid = false
  }

  if (!formData.value.postcode) {
    errors.value.postcode = 'Postcode is required'
    isValid = false
  }

  if (!formData.value.country) {
    errors.value.country = 'Country is required'
    isValid = false
  }

  // Course Interest validation
  if (!formData.value.studyLevel) {
    errors.value.studyLevel = 'Please select a level of study'
    isValid = false
  }

  if (!formData.value.subjectArea) {
    errors.value.subjectArea = 'Please select a subject area'
    isValid = false
  }

  // Event Details validation
  if (!formData.value.eventDate) {
    errors.value.eventDate = 'Please select an event date'
    isValid = false
  }

  if (!formData.value.guestCount && formData.value.guestCount !== 0) {
    errors.value.guestCount = 'Please select number of guests'
    isValid = false
  }

  // Check if at least one source is selected
  const anySourceSelected = Object.values(formData.value.sources).some((value) => value)
  if (!anySourceSelected) {
    errors.value.sources = 'Please select at least one option'
    isValid = false
  }

  if (!privacyPolicy.value) {
    errors.value.privacyPolicy = 'Please accept the privacy policy'
    isValid = false
  }

  return isValid
}

const submitForm = async () => {
  if (!validateForm()) {
    // Scroll to the first error
    const firstErrorElement = document.querySelector('.text-danger')
    if (firstErrorElement) {
      firstErrorElement.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }
    return
  }

  loading.value = true

  try {
    const payload = {
      personalDetails: {
        title: formData.value.title,
        firstName: formData.value.firstName,
        lastName: formData.value.lastName,
        dateOfBirth: formData.value.dob,
      },
      carerDetails: {
        firstName: formData.value.carerFirstName,
        lastName: formData.value.carerLastName,
        email: formData.value.carerEmail,
      },
      contactDetails: {
        email: formData.value.email,
        phoneNumber: formData.value.phone,
        address: {
          line1: formData.value.address1,
          line2: formData.value.address2 || '',
          city: formData.value.city,
          postcode: formData.value.postcode,
          country: formData.value.country,
        },
      },
      courseInterest: {
        levelOfStudy: formData.value.studyLevel,
        subjectArea: formData.value.subjectArea,
      },
      eventDetails: {
        date: formData.value.eventDate,
        guestCount: parseInt(formData.value.guestCount),
        marketingSources: Object.entries(formData.value.sources)
          .filter(([_, value]) => value)
          .map(([key]) => key),
      },
    }

    console.log('Submitting form with payload:', payload)

    const response = await api.post(
      '/registration',
      {
        ...payload,
      },
      {
        headers: {
          'Content-Type': 'application/json',
        },
      },
    )

    if (response.status !== 201) {
      throw new Error('Registration failed')
    }

    alert("Registration successful! Check your email for confirmation. We're looking forward to seeing you at the event.")

    // TODO: Handle successful registration; e.g., show success message, redirect to confirmation page

    resetForm()
  } catch (error) {
    console.error('Error submitting form:', error)
    errors.value.request = 'There was an error submitting your registration. Please try again.'
  } finally {
    loading.value = false
  }
}

const resetForm = () => {
  formData.value = {
    title: '',
    firstName: '',
    lastName: '',
    dob: '',
    email: '',
    phone: '',
    address1: '',
    address2: '',
    city: '',
    postcode: '',
    country: '',
    studyLevel: '',
    subjectArea: '',
    eventDate: '',
    guestCount: '',
    sources: {
      email: false,
      social: false,
      search: false,
      school: false,
      other: false,
    },
    carerFirstName: '',
    carerLastName: '',
    carerEmail: '',
  }
  carer.value = false
  privacyPolicy.value = false
  errors.value = {
    title: '',
    firstName: '',
    lastName: '',
    dob: '',
    email: '',
    phone: '',
    address1: '',
    address2: '',
    city: '',
    postcode: '',
    country: '',
    studyLevel: '',
    subjectArea: '',
    eventDate: '',
    guestCount: '',
    sources: '',
    carerFirstName: '',
    carerLastName: '',
    carerEmail: '',
    privacyPolicy: '',
    request: '',
  }
}
</script>
