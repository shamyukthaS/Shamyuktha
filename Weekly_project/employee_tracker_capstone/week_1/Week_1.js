use("employee_tracker");
db.employee_feedback.insertMany([
  { employee_id: 101, employee_name: "arun",    department: "it",        feedback: "excellent dashboard development and teamwork",   rating: 5 },
  { employee_id: 102, employee_name: "priya",   department: "hr",        feedback: "good recruitment performance",                  rating: 4 },
  { employee_id: 103, employee_name: "karthik", department: "finance",   feedback: "completed reports before deadline",             rating: 5 },
  { employee_id: 104, employee_name: "sana",    department: "marketing", feedback: "needs improvement in task completion",          rating: 2 },
  { employee_id: 105, employee_name: "rahul",   department: "sales",     feedback: "consistent performance and reporting",          rating: 4 },
  { employee_id: 106, employee_name: "meena",   department: "it",        feedback: "excellent bug fixing and testing",              rating: 5 },
  { employee_id: 107, employee_name: "vikram",  department: "finance",   feedback: "strong audit and compliance work",              rating: 5 },
  { employee_id: 108, employee_name: "divya",   department: "hr",        feedback: "good coordination and onboarding",             rating: 4 },
  { employee_id: 109, employee_name: "ajay",    department: "sales",     feedback: "top sales performer this month",               rating: 5 },
  { employee_id: 110, employee_name: "nisha",   department: "marketing", feedback: "attendance and productivity need improvement",  rating: 2 }
]);
print("✔ Feedback records inserted.\n");

print("--- Find employee 103 ---");
printjson(db.employee_feedback.findOne({ employee_id: 103 }));

print("\n--- All Finance department employees ---");
db.employee_feedback.find({ department: "finance" }).forEach(printjson);

db.employee_feedback.updateOne(
  { employee_id: 104 },
  { $set: { rating: 3, feedback: "showing improvement in task completion after coaching" } }
);
print("\n✔ Updated employee 104 (sana) rating to 3.\n");

db.employee_feedback.deleteOne({ employee_id: 110 });
print("✔ Deleted employee 110 (nisha) record.\n");

db.attendance.insertMany([
  { employee_id: 101, employee_name: "arun",    date: "2025-06-01", clock_in: "09:00", clock_out: "18:00", total_hours: 9,   status: "present" },
  { employee_id: 102, employee_name: "priya",   date: "2025-06-01", clock_in: "09:15", clock_out: "17:45", total_hours: 8.5, status: "present" },
  { employee_id: 103, employee_name: "karthik", date: "2025-06-01", clock_in: null,    clock_out: null,    total_hours: 0,   status: "absent"  },
  { employee_id: 104, employee_name: "sana",    date: "2025-06-01", clock_in: "10:30", clock_out: "17:00", total_hours: 6.5, status: "late"    },
  { employee_id: 105, employee_name: "rahul",   date: "2025-06-01", clock_in: "09:00", clock_out: "18:00", total_hours: 9,   status: "present" },
  { employee_id: 106, employee_name: "meena",   date: "2025-06-01", clock_in: "08:45", clock_out: "17:45", total_hours: 9,   status: "present" },
  { employee_id: 107, employee_name: "vikram",  date: "2025-06-01", clock_in: "09:00", clock_out: "18:30", total_hours: 9.5, status: "present" },
  { employee_id: 108, employee_name: "divya",   date: "2025-06-01", clock_in: null,    clock_out: null,    total_hours: 0,   status: "absent"  },
  { employee_id: 109, employee_name: "ajay",    date: "2025-06-01", clock_in: "09:05", clock_out: "18:05", total_hours: 9,   status: "present" },
  { employee_id: 101, employee_name: "arun",    date: "2025-06-02", clock_in: "09:10", clock_out: "18:10", total_hours: 9,   status: "present" },
  { employee_id: 103, employee_name: "karthik", date: "2025-06-02", clock_in: "09:00", clock_out: "17:00", total_hours: 8,   status: "present" },
  { employee_id: 104, employee_name: "sana",    date: "2025-06-02", clock_in: null,    clock_out: null,    total_hours: 0,   status: "absent"  },
  { employee_id: 108, employee_name: "divya",   date: "2025-06-02", clock_in: "09:30", clock_out: "17:30", total_hours: 8,   status: "present" }
]);
print("✔ Attendance records inserted.\n");

db.attendance.insertOne({
  employee_id: 105,
  employee_name: "rahul",
  date: "2025-06-02",
  clock_in: "09:00",
  clock_out: null,
  total_hours: 0,
  status: "present"
});
print("✔ Clock-in recorded for employee 105 (rahul) on 2025-06-02.\n");

db.attendance.updateOne(
  { employee_id: 105, date: "2025-06-02", clock_out: null },
  { $set: { clock_out: "18:00", total_hours: 9 } }
);
print("✔ Clock-out recorded for employee 105 (rahul) on 2025-06-02.\n");

db.tasks.insertMany([
  {
    employee_id: 101, employee_name: "arun", department: "it",
    task_title: "Dashboard Revamp",
    notes: "Completed UI redesign using React. Integrated new API endpoints. Reviewed by team lead and approved.",
    status: "completed", priority: "high",
    assigned_date: "2025-05-20", due_date: "2025-05-30", completed_date: "2025-05-28",
    tags: ["react", "api", "ui"]
  },
  {
    employee_id: 102, employee_name: "priya", department: "hr",
    task_title: "Q2 Recruitment Drive",
    notes: "Screened 40 candidates. Scheduled 15 interviews. 5 offers extended. Follow-up pending for 3 candidates.",
    status: "in-progress", priority: "high",
    assigned_date: "2025-06-01", due_date: "2025-06-15", completed_date: null,
    tags: ["recruitment", "interviews", "hiring"]
  },
  {
    employee_id: 103, employee_name: "karthik", department: "finance",
    task_title: "Monthly Financial Report",
    notes: "All expense sheets compiled. Variance analysis done. Report submitted 2 days ahead of deadline.",
    status: "completed", priority: "critical",
    assigned_date: "2025-05-25", due_date: "2025-06-01", completed_date: "2025-05-30",
    tags: ["finance", "reporting", "audit"]
  },
  {
    employee_id: 104, employee_name: "sana", department: "marketing",
    task_title: "Social Media Campaign",
    notes: "Campaign draft delayed. Content not submitted on time. Manager notified. Needs follow-up and stricter deadline management.",
    status: "delayed", priority: "medium",
    assigned_date: "2025-05-28", due_date: "2025-06-03", completed_date: null,
    tags: ["marketing", "social-media", "campaign"]
  },
  {
    employee_id: 105, employee_name: "rahul", department: "sales",
    task_title: "Client Follow-up Q2",
    notes: "Contacted 25 existing clients. Renewed 10 contracts. 3 new leads added to pipeline. Weekly report submitted.",
    status: "completed", priority: "high",
    assigned_date: "2025-06-01", due_date: "2025-06-07", completed_date: "2025-06-06",
    tags: ["sales", "clients", "contracts"]
  },
  {
    employee_id: 106, employee_name: "meena", department: "it",
    task_title: "Bug Fix - Payment Module",
    notes: "Identified 3 critical bugs in the payment gateway. Fixed and deployed to staging. QA sign-off received.",
    status: "completed", priority: "critical",
    assigned_date: "2025-05-29", due_date: "2025-06-02", completed_date: "2025-06-01",
    tags: ["bugfix", "payment", "qa"]
  },
  {
    employee_id: 107, employee_name: "vikram", department: "finance",
    task_title: "Compliance Audit",
    notes: "Internal audit completed for Q1. All documents verified. No discrepancies found. Submitted to external auditor.",
    status: "completed", priority: "critical",
    assigned_date: "2025-05-15", due_date: "2025-06-01", completed_date: "2025-05-30",
    tags: ["audit", "compliance", "finance"]
  },
  {
    employee_id: 108, employee_name: "divya", department: "hr",
    task_title: "New Employee Onboarding",
    notes: "Onboarded 3 new employees. Documents collected and verified. System access granted. Orientation scheduled.",
    status: "in-progress", priority: "medium",
    assigned_date: "2025-06-01", due_date: "2025-06-10", completed_date: null,
    tags: ["onboarding", "hr", "orientation"]
  },
  {
    employee_id: 109, employee_name: "ajay", department: "sales",
    task_title: "Enterprise Sales Target",
    notes: "Exceeded monthly target by 120%. Closed 2 enterprise deals. Highest performer in the sales team this month.",
    status: "completed", priority: "high",
    assigned_date: "2025-06-01", due_date: "2025-06-30", completed_date: "2025-06-15",
    tags: ["sales", "enterprise", "target"]
  }
]);
print("✔ Task records inserted.\n");

db.employee_feedback.createIndex({ employee_id: 1 });
db.employee_feedback.createIndex({ department: 1 });
db.employee_feedback.createIndex({ rating: -1 });

db.attendance.createIndex({ employee_id: 1 });
db.attendance.createIndex({ date: 1 });
db.attendance.createIndex({ employee_id: 1, date: 1 });
db.attendance.createIndex({ status: 1 });

db.tasks.createIndex({ employee_id: 1 });
db.tasks.createIndex({ department: 1 });
db.tasks.createIndex({ status: 1 });
db.tasks.createIndex({ priority: 1 });

print("✔ All indexes created.\n");

print("--- Feedback Indexes ---");
printjson(db.employee_feedback.getIndexes());

print("\n--- Attendance Indexes ---");
printjson(db.attendance.getIndexes());

print("\n--- Tasks Indexes ---");
printjson(db.tasks.getIndexes());

function calculateTotalWorkingHours(employeeId) {
  var result = db.attendance.aggregate([
    { $match: { employee_id: employeeId } },
    {
      $group: {
        _id: "$employee_id",
        employee_name: { $first: "$employee_name" },
        total_hours:   { $sum: "$total_hours" },
        days_present:  { $sum: { $cond: [{ $eq: ["$status", "present"] }, 1, 0] } },
        days_absent:   { $sum: { $cond: [{ $eq: ["$status", "absent"]  }, 1, 0] } },
        days_late:     { $sum: { $cond: [{ $eq: ["$status", "late"]    }, 1, 0] } }
      }
    }
  ]).toArray();

  if (result.length === 0) {
    print("No attendance records found for employee_id: " + employeeId);
    return null;
  }
  return result[0];
}

print("\n=== Working Hours Report for Employee 101 ===");
printjson(calculateTotalWorkingHours(101));

print("\n=== Working Hours Report for Employee 104 ===");
printjson(calculateTotalWorkingHours(104));

print("\n========== REPORT 1: Avg Rating by Department ==========");
db.employee_feedback.aggregate([
  {
    $group: {
      _id: "$department",
      avg_rating:      { $avg: "$rating" },
      total_employees: { $sum: 1 }
    }
  },
  { $sort: { avg_rating: -1 } }
]).forEach(printjson);

print("\n========== REPORT 2: Absenteeism Report ==========");
db.attendance.aggregate([
  { $match: { status: "absent" } },
  {
    $group: {
      _id: "$employee_id",
      employee_name: { $first: "$employee_name" },
      absent_days:   { $sum: 1 }
    }
  },
  { $sort: { absent_days: -1 } }
]).forEach(function(doc) {
  print("Employee: " + doc.employee_name + " | Absent Days: " + doc.absent_days);
});

print("\n========== REPORT 3: Underperformance Report (Rating <= 3) ==========");
db.employee_feedback.find(
  { rating: { $lte: 3 } },
  { _id: 0, employee_name: 1, department: 1, rating: 1, feedback: 1 }
).forEach(function(doc) {
  print("* " + doc.employee_name + " (" + doc.department + ") - Rating: " + doc.rating);
  print("  Feedback: " + doc.feedback);
});

print("\n========== REPORT 4: Task Completion Report ==========");
db.tasks.aggregate([
  {
    $group: {
      _id: "$status",
      count:     { $sum: 1 },
      employees: { $push: "$employee_name" }
    }
  },
  { $sort: { count: -1 } }
]).forEach(printjson);

print("\n========== REPORT 5: Top Performers (Rating = 5) ==========");
db.employee_feedback.find(
  { rating: 5 },
  { _id: 0, employee_name: 1, department: 1, feedback: 1 }
).forEach(function(doc) {
  print("* " + doc.employee_name + " (" + doc.department + "): " + doc.feedback);
});

print("\n========== REPORT 6: Full Employee Summary ==========");
var employeeIds = db.employee_feedback.distinct("employee_id");

employeeIds.forEach(function(empId) {
  var feedback   = db.employee_feedback.findOne({ employee_id: empId });
  var attendance = db.attendance.aggregate([
    { $match: { employee_id: empId } },
    {
      $group: {
        _id: null,
        total_hours: { $sum: "$total_hours" },
        absences:    { $sum: { $cond: [{ $eq: ["$status", "absent"] }, 1, 0] } }
      }
    }
  ]).toArray()[0];

  var tasks          = db.tasks.find({ employee_id: empId }).toArray();
  var completedTasks = tasks.filter(function(t) { return t.status === "completed"; }).length;

  print("-------------------------------------");
  print("Employee : " + feedback.employee_name + " (ID: " + empId + ")");
  print("Dept     : " + feedback.department);
  print("Rating   : " + feedback.rating + "/5");
  print("Hours    : " + (attendance ? attendance.total_hours : "N/A"));
  print("Absences : " + (attendance ? attendance.absences   : "N/A") + " day(s)");
  print("Tasks    : " + completedTasks + "/" + tasks.length + " completed");
  print("Feedback : " + feedback.feedback);
});
db.attendance.updateMany(
 { date: "2025-06-01" },
 { $set: { date: "2026-06-01" } }
)

db.attendance.updateMany(
 { date: "2025-06-02" },
 { $set: { date: "2026-06-02" } }
)

db.attendance.find(
 {},
 {
   _id:0,
   employee_id:1,
   date:1
 }
)

db.tasks.updateMany(
 {},
 [
   {
     $set: {
       assigned_date: {
         $replaceOne: {
           input: "$assigned_date",
           find: "2025",
           replacement: "2026"
         }
       }
     }
   }
 ]
)

db.tasks.updateMany(
 {},
 [
   {
     $set: {
       due_date: {
         $replaceOne: {
           input: "$due_date",
           find: "2025",
           replacement: "2026"
         }
       }
     }
   }
 ]
)

db.tasks.updateMany(
 { completed_date: { $ne: null } },
 [
   {
     $set: {
       completed_date: {
         $replaceOne: {
           input: "$completed_date",
           find: "2025",
           replacement: "2026"
         }
       }
     }
   }
 ]
)

db.tasks.find(
 {},
 {
   _id:0,
   employee_id:1,
   assigned_date:1,
   due_date:1,
   completed_date:1
 }
)

print("\n=== All operations completed successfully. ===");


