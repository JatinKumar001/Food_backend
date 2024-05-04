import { spawn } from "child_process"

let title;

export const updaterecommendation = (req, res) => {

    const { title1 } = req.body;
    // console.log(title1)
    title = title1

    res.json({ message: 'Ingredients updated successfully' });
}

export const getfoodrecommendation = (req, res) => {
    const childPython = spawn('python', ['foodrecommendation.py', title]);

    childPython.stdout.on('data', (data) => {
        // console.log(`${data}`)
        try{
            res.send(data);
        }
        catch (err) {
            res.status(500).json(err);
        }
    })
}