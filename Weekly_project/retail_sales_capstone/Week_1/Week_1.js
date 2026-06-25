use retail_sales_dashboard
db.createCollection("campaign_feedback")
db.campaign_feedback.insertMany([
  {
    campaign_id: 1,
    product: "Laptop",
    region: "South",
    feedback: "Strong customer response",
    rating: 4.5,
    tags: ["electronics", "high-demand"]
  },
  {
    campaign_id: 2,
    product: "T-Shirt",
    region: "North",
    feedback: "Moderate interest during festive season",
    rating: 3.2,
    tags: ["clothing", "seasonal"]
  },
  {
    campaign_id: 3,
    product: "Rice 5kg",
    region: "South",
    feedback: "Consistent sales, low margin",
    rating: 3.8,
    tags: ["grocery", "staple"]
  },
  {
    campaign_id: 4,
    product: "Laptop",
    region: "North",
    feedback: "Low footfall but high conversion rate",
    rating: 4.0,
    tags: ["electronics", "low-traffic"]
  },
  {
    campaign_id: 5,
    product: "T-Shirt",
    region: "South",
    feedback: "Discount drove bulk purchases",
    rating: 4.2,
    tags: ["clothing", "discount"]
  }
])

db.campaign_feedback.createIndex({ product: 1 })
db.campaign_feedback.createIndex({ region: 1 })
db.campaign_feedback.getIndexes()
db.campaign_feedback.find({ product: "Laptop" })
db.campaign_feedback.find({ region: "South" })
db.campaign_feedback.find({ product: "Laptop", region: "South" })
db.campaign_feedback.find({ rating: { $gt: 4.0 } })
db.campaign_feedback.countDocuments()
