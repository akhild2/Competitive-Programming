const fs = require('fs')

function findDuplicateFiles(startingDirectory) {
  let seen = {},
      stack = [startingDirectory],
      ans = [];

  while (stack.length) {
    let thisPath = stack.pop(),
        thisFile = fs.statSync(thisPath);

    if (thisFile.isDirectory()) {
      fs.readdirSync(thisPath).forEach((path) => {
        stack.push(thisPath + '/' + path);
      });
      
    } else {
      let fileContents = fs.readFileSync(thisPath),
          lastEditedTime = thisFile.mtime;

      if(seen.hasOwnProperty(fileContents)){
        let currentFile = seen[fileContents];
        
        if (lastEditedTime > currentFile.lastEditedTime) {
          ans.push([thisPath, currentFile.path]);
        } else {
          ans.push([currentFile.path, thisPath]);
          seen[fileContents] = {lastEditedTime: lastEditedTime, path: thisPath}
        }
        
      } else {
        seen[fileContents] = {lastEditedTime: lastEditedTime, path: thisPath}
      }
    }
  }
  return ans;
}