properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone") {
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MichaelRing81/DevOps1411.git']]])
    }
    stage("show files"){
        bat "dir"
    }
}
