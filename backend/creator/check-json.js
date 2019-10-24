
function checkjson(json){
    // const json = JSON.parse(data)
    const {
        // selectedTemplate = 1,
        basics = {},
        education = [],
        work = [],
        skills = [],
        projects = [],
        awards = []
    } = json

    const validJSON = {
        // selectedTemplate,
        basics,
        education,
        work,
        skills,
        projects,
        awards
    }

    return validJSON
}

exports.checkjson = checkjson