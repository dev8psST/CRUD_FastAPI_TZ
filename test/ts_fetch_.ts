import axios from 'axios';


interface User {
  id: number;
  email: string;
  city: string;
  name: string;
  date_register: string;
  salary_in_year: number;
  number_phone: string;
}


async function fetchData() {
  const response = await axios.get('http://localhost:8000/user_data');
  
  const d = response.data  as User[];
  console.log(response.data);
  console.log(d[0].name);
  console.log(d[1].name);
}

fetchData();

/* 


npm init -y

npm install axios

npm install --save-dev @types/node

npm install --save-dev @types/axios

npm install --save-dev typescript

npx tsc --init

npx tsc

node your_compiled_file.js

npm init -y && npm install axios && npm install -D typescript @types/node @types/axios && npx tsc --init


"scripts": {
  "start": "npx tsc && node dist/index.js"
}

npm run start
*/
