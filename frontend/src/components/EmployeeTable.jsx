import { useEffect, useState } from "react";
import api from "../api";
import { toast } from "react-toastify";

const initialForm = {
  emp_code: "",
  name: "",
  department: "",
  designation: "",
  email: "",
  phone: "",
  basic_salary: "",
  hra: "",
  da: "",
  bonus: ""
};

export default function EmployeeTable() {
  const [data, setData] = useState([]);
  const [form, setForm] = useState(initialForm);

  const loadEmployees = () => {
    api.get("/employees")
      .then(res => setData(res.data));
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  const onChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const addEmployee = async () => {
    try {
      await api.post("/employees", {
        ...form,
        basic_salary: Number(form.basic_salary),
        hra: Number(form.hra),
        da: Number(form.da),
        bonus: Number(form.bonus)
      });

      toast.success("Employee added");
      setForm(initialForm);
      loadEmployees();
    } catch {
      toast.error("Add failed");
    }
  };

  const deleteEmployee = async (id) => {
    try {
      await api.delete(`/employees/${id}`);
      toast.success("Employee deleted");
      loadEmployees();
    } catch {
      toast.error("Delete failed");
    }
  };

  return (
    <>
      <div className="table-box" style={{ marginBottom: "25px" }}>
        <h2>Add Employee</h2>
        <br />

        <input name="emp_code" placeholder="Employee Code" value={form.emp_code} onChange={onChange}/>
        <input name="name" placeholder="Name" value={form.name} onChange={onChange}/>
        <input name="department" placeholder="Department" value={form.department} onChange={onChange}/>
        <input name="designation" placeholder="Designation" value={form.designation} onChange={onChange}/>
        <input name="email" placeholder="Email" value={form.email} onChange={onChange}/>
        <input name="phone" placeholder="Phone" value={form.phone} onChange={onChange}/>
        <input name="basic_salary" placeholder="Basic Salary" value={form.basic_salary} onChange={onChange}/>
        <input name="hra" placeholder="HRA" value={form.hra} onChange={onChange}/>
        <input name="da" placeholder="DA" value={form.da} onChange={onChange}/>
        <input name="bonus" placeholder="Bonus" value={form.bonus} onChange={onChange}/>

        <button onClick={addEmployee}>Add Employee</button>
      </div>

      <div className="table-box">
        <h2>Employees</h2>
        <br />

        <table>
          <thead>
            <tr>
              <th>Code</th>
              <th>Name</th>
              <th>Department</th>
              <th>Designation</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            {data.map(e => (
              <tr key={e.id}>
                <td>{e.emp_code}</td>
                <td>{e.name}</td>
                <td>{e.department}</td>
                <td>{e.designation}</td>
                <td>
                  <button
                    style={{ width: "90px" }}
                    onClick={() => deleteEmployee(e.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}