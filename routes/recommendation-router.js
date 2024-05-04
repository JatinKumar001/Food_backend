import express from 'express'
import { getfoodrecommendation, updaterecommendation } from '../conttollers/recommendation-controller.js';

const router = express.Router();

router.post("/", updaterecommendation);
router.get("/", getfoodrecommendation);

export default router