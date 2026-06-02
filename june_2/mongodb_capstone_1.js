use("food_delivery_capstone_db");

db.customers.insertMany([
  { customer_id: 1, name: "Rahul Sharma", city: "Hyderabad", membership: "Gold", phone: "9876543210" },
  { customer_id: 2, name: "Priya Reddy", city: "Bangalore", membership: "Silver", phone: "9876543211" },
  { customer_id: 3, name: "Amit Kumar", city: "Mumbai", membership: "Gold", phone: null },
  { customer_id: 4, name: "Sneha Patel", city: "Chennai", membership: "Bronze", phone: "9876543213" },
  { customer_id: 5, name: "Arjun Verma", city: "Delhi", membership: "Silver", phone: "9876543214" }
]);

db.restaurants.insertMany([
  { restaurant_id: 101, name: "Spice Hub", city: "Hyderabad", cuisine: "Indian", rating: 4.5 },
  { restaurant_id: 102, name: "Pizza Corner", city: "Bangalore", cuisine: "Italian", rating: 4.2 },
  { restaurant_id: 103, name: "Green Bowl", city: "Chennai", cuisine: "Healthy", rating: 4.7 },
  { restaurant_id: 104, name: "Burger Street", city: "Mumbai", cuisine: "Fast Food", rating: 3.9 },
  { restaurant_id: 105, name: "Royal Tandoor", city: "Delhi", cuisine: "Indian", rating: 4.8 }
]);

db.delivery_partners.insertMany([
  { partner_id: 201, partner_name: "FastMove Logistics", city: "Hyderabad", rating: 4.4 },
  { partner_id: 202, partner_name: "QuickShip", city: "Bangalore", rating: 4.1 },
  { partner_id: 203, partner_name: "SpeedKart", city: "Mumbai", rating: 4.6 },
  { partner_id: 204, partner_name: "DoorDash India", city: "Delhi", rating: 4.0 }
]);

db.orders.insertMany([
  {
    order_id: 1001, customer_id: 1, restaurant_id: 101, partner_id: 201,
    items: [{ item_name: "Biryani", quantity: 2, price: 250 }, { item_name: "Kebab", quantity: 1, price: 180 }],
    order_amount: 680, payment: { mode: "UPI", status: "Success" },
    order_status: "Delivered", delivery_time_minutes: 35, order_rating: 5
  },
  {
    order_id: 1002, customer_id: 2, restaurant_id: 102, partner_id: 202,
    items: [{ item_name: "Pizza", quantity: 1, price: 500 }, { item_name: "Garlic Bread", quantity: 1, price: 150 }],
    order_amount: 650, payment: { mode: "Card", status: "Success" },
    order_status: "Delivered", delivery_time_minutes: 42, order_rating: 4
  },
  {
    order_id: 1003, customer_id: 3, restaurant_id: 104, partner_id: 203,
    items: [{ item_name: "Burger", quantity: 2, price: 180 }, { item_name: "Fries", quantity: 1, price: 120 }],
    order_amount: 480, payment: { mode: "Cash", status: "Pending" },
    order_status: "Pending", delivery_time_minutes: null, order_rating: null
  },
  {
    order_id: 1004, customer_id: 4, restaurant_id: 103, partner_id: null,
    items: [{ item_name: "Salad Bowl", quantity: 1, price: 350 }],
    order_amount: 350, payment: { mode: "UPI", status: "Failed" },
    order_status: "Cancelled", delivery_time_minutes: null, order_rating: null
  },
  {
    order_id: 1005, customer_id: 5, restaurant_id: 105, partner_id: 204,
    items: [{ item_name: "Tandoori Chicken", quantity: 1, price: 600 }, { item_name: "Naan", quantity: 2, price: 60 }],
    order_amount: 720, payment: { mode: "UPI", status: "Success" },
    order_status: "Delivered", delivery_time_minutes: 50, order_rating: 5
  },
  {
    order_id: 1006, customer_id: 1, restaurant_id: 101, partner_id: 201,
    items: [{ item_name: "Paneer Curry", quantity: 1, price: 300 }, { item_name: "Roti", quantity: 4, price: 25 }],
    order_amount: 400, payment: { mode: "Card", status: "Success" },
    order_status: "Delivered", delivery_time_minutes: 30, order_rating: 4
  }
]);

db.customers.find();

db.restaurants.find();

db.customers.find({}, { _id: 0, name: 1, city: 1, membership: 1 });

db.customers.find({ city: "Hyderabad" });

db.customers.find({ membership: "Gold" });

db.restaurants.find({ rating: { $gt: 4.5 } });

db.orders.find({ order_amount: { $gt: 500 } });

db.orders.find({ order_status: "Delivered" });

db.orders.find({ order_status: "Cancelled" });

db.customers.find({ phone: null });

db.orders.find({ order_amount: { $gte: 400, $lte: 700 } });

db.customers.find({ city: { $in: ["Hyderabad", "Delhi", "Mumbai"] } });

db.restaurants.find({ cuisine: { $in: ["Indian", "Fast Food"] } });

db.orders.find({ "payment.status": { $ne: "Success" } });

db.orders.find({ delivery_time_minutes: null });

db.orders.find({ order_rating: { $gte: 4 } });

db.restaurants.find({ city: { $nin: ["Bangalore", "Chennai"] } });

db.orders.find({ "items.item_name": "Biryani" });

db.orders.find({ "items.item_name": "Pizza" });

db.orders.find({ "items.quantity": { $gt: 1 } });

db.orders.find({ "items.price": { $gt: 300 } });

db.orders.find({}, { _id: 0, order_id: 1, items: 1 });

db.restaurants.find().sort({ rating: -1 });

db.restaurants.find().sort({ rating: -1 }).limit(3);

db.orders.find().sort({ order_amount: -1 });

db.orders.find().sort({ order_amount: -1 }).limit(2);

db.delivery_partners.find().sort({ rating: -1 });

db.customers.updateOne({ customer_id: 1 }, { $set: { membership: "Platinum" } });

db.restaurants.updateOne({ restaurant_id: 104 }, { $set: { rating: 4.1 } });

db.orders.updateOne({ order_id: 1003 }, { $set: { order_status: "Delivered" } });

db.orders.updateOne({ order_id: 1003 }, { $set: { delivery_time_minutes: 45 } });

db.customers.updateMany({}, { $set: { active: true } });

db.customers.updateMany({}, { $unset: { active: "" } });

db.orders.updateOne(
  { order_id: 1006 },
  { $push: { items: { item_name: "Curd Rice", quantity: 1, price: 120 } } }
);

db.orders.deleteMany({ order_status: "Cancelled" });

db.restaurants.deleteMany({ rating: { $lt: 4.0 } });

db.customers.countDocuments();

db.orders.countDocuments();

db.orders.countDocuments({ order_status: "Delivered" });

db.orders.countDocuments({ "payment.status": "Failed" });

db.customers.distinct("city");

db.restaurants.distinct("cuisine");

db.orders.distinct("payment.mode");

db.orders.aggregate([
  { $match: { "payment.status": "Success" } },
  { $group: { _id: "$payment.mode", total_revenue: { $sum: "$order_amount" } } }
]);

db.orders.aggregate([
  { $group: { _id: "$order_status", total_revenue: { $sum: "$order_amount" } } }
]);

db.orders.aggregate([
  { $match: { order_status: "Delivered", delivery_time_minutes: { $ne: null } } },
  { $group: { _id: null, avg_delivery_time: { $avg: "$delivery_time_minutes" } } }
]);

db.orders.aggregate([
  { $group: { _id: "$customer_id", total_orders: { $sum: 1 }, total_amount: { $sum: "$order_amount" } } }
]);

db.orders.aggregate([
  { $group: { _id: "$restaurant_id", total_orders: { $sum: 1 }, total_revenue: { $sum: "$order_amount" } } }
]);

db.orders.aggregate([
  { $match: { order_rating: { $ne: null } } },
  { $group: { _id: "$restaurant_id", avg_rating: { $avg: "$order_rating" } } }
]);

db.orders.aggregate([
  { $group: { _id: "$customer_id", total_spending: { $sum: "$order_amount" } } },
  { $match: { total_spending: { $gt: 700 } } }
]);

db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer_info"
    }
  },
  { $unwind: "$customer_info" },
  {
    $project: {
      _id: 0,
      order_id: 1,
      customer_name: "$customer_info.name",
      city: "$customer_info.city",
      order_amount: 1,
      order_status: 1
    }
  }
]);

db.orders.aggregate([
  {
    $lookup: {
      from: "restaurants",
      localField: "restaurant_id",
      foreignField: "restaurant_id",
      as: "restaurant_info"
    }
  },
  { $unwind: "$restaurant_info" },
  {
    $project: {
      _id: 0,
      order_id: 1,
      restaurant_name: "$restaurant_info.name",
      cuisine: "$restaurant_info.cuisine",
      order_amount: 1
    }
  }
]);

db.orders.aggregate([
  {
    $lookup: {
      from: "delivery_partners",
      localField: "partner_id",
      foreignField: "partner_id",
      as: "partner_info"
    }
  },
  { $unwind: { path: "$partner_info", preserveNullAndEmptyArrays: true } },
  {
    $project: {
      _id: 0,
      order_id: 1,
      partner_name: "$partner_info.partner_name",
      delivery_time: "$delivery_time_minutes",
      order_status: 1
    }
  }
]);

db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer_info"
    }
  },
  { $unwind: "$customer_info" },
  {
    $lookup: {
      from: "restaurants",
      localField: "restaurant_id",
      foreignField: "restaurant_id",
      as: "restaurant_info"
    }
  },
  { $unwind: "$restaurant_info" },
  {
    $lookup: {
      from: "delivery_partners",
      localField: "partner_id",
      foreignField: "partner_id",
      as: "partner_info"
    }
  },
  { $unwind: { path: "$partner_info", preserveNullAndEmptyArrays: true } },
  {
    $project: {
      _id: 0,
      order_id: 1,
      customer_name: "$customer_info.name",
      restaurant_name: "$restaurant_info.name",
      cuisine: "$restaurant_info.cuisine",
      partner_name: "$partner_info.partner_name",
      order_amount: 1,
      payment_mode: "$payment.mode",
      payment_status: "$payment.status",
      order_status: 1,
      delivery_time: "$delivery_time_minutes",
      rating: "$order_rating"
    }
  }
]);
